from typing import Literal
import numpy as np
import pandas as pd


def data_generating_process(
    n: int,
    setting: str,
    seed: int = 123,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Generate a synthetic dataset for uplift modeling in a lodging marketplace.

    Out of the two frames that are returned, `data` is the one that would be available
    in practice, as meta_data contains counterfactual information.

    Args:
        n: number of samples
        setting: "observational" (targeted, unbalanced) or "rct" (balanced 50/50)
        seed: the random seed

    Returns:
        data: The actual dataset used for modeling, with the following columns:
            - client_id: unique identifier for each sample
            - Y: conversion result [binary, 0/1]
            - T: treatment [binary, 0/1]
            - Various features commonly available on ecommerce platforms
        meta_data: Information NOT available in practice, but useful for validation:
            - client_id: unique identifier for each sample
            - Y: conversion result [binary, 0/1]
            - T: treatment [binary, 0/1]
            - p_treat: treatment propensity used in generation
            - true_p_y0: conversion probability if untreated
            - true_p_y1: conversion probability if treated
            - true_uplift: true individual uplift (p_y1 - p_y0)
    """

    def sigmoid(z):
        return 1.0 / (1.0 + np.exp(-z))

    rng = np.random.default_rng(seed)

    channels = np.array(["paid_search", "organic", "email", "direct", "app_push"])
    devices = np.array(["mobile_web", "desktop", "app"])
    dest_tiers = np.array(["tier1", "tier2", "tier3"])

    # --- Draw base features ---
    channel = rng.choice(channels, size=n, p=[0.35, 0.25, 0.15, 0.20, 0.05])
    device = rng.choice(devices, size=n, p=[0.55, 0.30, 0.15])
    dest_tier = rng.choice(dest_tiers, size=n, p=[0.50, 0.35, 0.15])

    # Lead time (days to check-in): empirical-ish discrete distribution
    lead_time = np.clip(
        rng.choice(
            [0, 1, 2, 3, 5, 7, 10, 14, 21, 30, 45, 60, 90, 120],
            size=n,
            p=[0.06, 0.05, 0.05, 0.05, 0.07, 0.07, 0.08, 0.09, 0.11, 0.12, 0.09, 0.07, 0.05, 0.04],
        ),
        0,
        120,
    )

    # Funnel depth: 0=landing, 1=search, 2=property details, 3=checkout
    funnel_depth = rng.choice([0, 1, 2, 3], size=n, p=[0.25, 0.40, 0.28, 0.07])

    # Behavioral/identity features
    price_sort_used = rng.binomial(1, p=0.35 + 0.15 * (channel == "paid_search"))
    past_coupon_user = rng.binomial(1, p=0.25 + 0.10 * (channel == "email"))
    tenure_days = rng.integers(0, 1800, size=n)
    hour_local = rng.integers(0, 24, size=n)

    # Recent ad exposure (helps form confounding in observational setting)
    recent_ad_exposure = rng.binomial(1, p=0.20 + 0.25 * (channel == "paid_search"))

    # --- Treatment assignment ---
    if setting == "observational":
        # Higher propensity for price-sensitive & shallow-funnel sessions, paid channels, recent exposure
        logit_p_treat = (
            -3.0
            + 1.2 * (channel == "paid_search")
            + 0.6 * (channel == "email")
            + 0.5 * (price_sort_used == 1)
            + 0.4 * (past_coupon_user == 1)
            + 0.5 * (funnel_depth == 0)
            + 0.3 * (funnel_depth == 1)
            - 0.3 * (funnel_depth == 3)
            + 0.2 * ((lead_time >= 8) & (lead_time <= 60))
            + 0.8 * (recent_ad_exposure == 1)
            - 0.2 * (device == "app")
        )
        p_treat = sigmoid(logit_p_treat)
        T = rng.binomial(1, p_treat)
    elif setting == "rct":
        p_treat = np.full(n, 0.5)
        T = rng.binomial(1, 0.5, size=n)
    else:
        raise ValueError("setting must be 'observational' or 'rct'")

    # --- Outcome model (potential outcomes) ---
    # Lead-time buckets for nonlinearity
    lt_0_1 = (lead_time <= 1).astype(float)
    lt_2_7 = ((lead_time >= 2) & (lead_time <= 7)).astype(float)
    lt_8_30 = ((lead_time >= 8) & (lead_time <= 30)).astype(float)
    lt_31_90 = ((lead_time >= 31) & (lead_time <= 90)).astype(float)
    lt_91_120 = ((lead_time >= 91) & (lead_time <= 120)).astype(float)

    # Baseline conversion log-odds (no coupon)
    baseline_logit = (
        -3.5
        + 0.2 * (device == "desktop")
        + 0.1 * (device == "app")
        + 0.4 * (dest_tier == "tier1")
        + 0.2 * (dest_tier == "tier2")
        + 0.15 * lt_0_1
        + 0.05 * lt_2_7
        + 0.0 * lt_8_30
        - 0.05 * lt_31_90
        - 0.1 * lt_91_120
        + 0.5 * (funnel_depth == 1)
        + 1.2 * (funnel_depth == 2)
        + 2.0 * (funnel_depth == 3)
        + 0.0002 * tenure_days
        + 0.05 * np.cos(2 * np.pi * hour_local / 24.0)
    )

    # True treatment effect on log-odds (uplift_logit): depends on realistic, not all, features
    uplift_logit = (
        0.45 * (price_sort_used == 1)
        + 1.35 * (channel == "paid_search")
        + 0.20 * (channel == "email")
        + 0.25 * ((lead_time >= 8) & (lead_time <= 60))
        + 0.50 * (funnel_depth == 0)
        + 0.15 * (funnel_depth == 1)
        - 0.20 * (funnel_depth == 3)
        - 0.25 * (past_coupon_user == 1)
        - 0.15 * (device == "app")  # app users a bit less elastic
        + 0.05
        * ((price_sort_used == 1) & ((lead_time >= 8) & (lead_time <= 60)))  # mild interaction
    )

    # Mild idiosyncratic noise
    rng_noise = np.random.default_rng(seed + 13)
    uplift_logit += rng_noise.normal(0, 0.02, size=n)

    # Potential outcomes
    logit_y0 = baseline_logit
    logit_y1 = baseline_logit + uplift_logit
    p_y0 = sigmoid(logit_y0)
    p_y1 = sigmoid(logit_y1)

    # Realized outcome given treatment
    Y = rng.binomial(1, np.where(T == 1, p_y1, p_y0))

    data = pd.DataFrame(
        {
            "client_id": np.arange(n),
            "Y": Y,
            "T": T,
            "true_uplift": p_y1 - p_y0,
            "channel": channel,
            "device": device,
            "lead_time": lead_time,
            "funnel_depth": funnel_depth,
            "price_sort_used": price_sort_used,
            "past_coupon_user": past_coupon_user,
            "tenure_days": tenure_days,
            "dest_tier": dest_tier,
            "hour_local": hour_local,
            "recent_ad_exposure": recent_ad_exposure,
        }
    )
    meta_data = pd.DataFrame(
        {
            "client_id": np.arange(n),
            "Y": Y,
            "T": T,
            "p_treat": p_treat,
            "true_p_y0": p_y0,
            "true_p_y1": p_y1,
            "true_uplift": p_y1 - p_y0,
        }
    )
    return data, meta_data


def binned_validation(
    y_true: np.ndarray,
    scores: dict[str, np.ndarray],
    bin_var: Literal["true", "pred"] = "true",
    n_bins: int = 20,
) -> pd.DataFrame:
    """Binned validation plot for multiple models.

    Build shared bins across multiple prediction arrays using the mean rank
    across models, then compute per-bin mean true uplift and per-model mean predictions.

    Returns a long DataFrame with columns:['bin', 'model', 'mean_true', 'mean_pred', 'count'].
    """
    # Validate lengths
    n = len(y_true)
    for k, v in scores.items():
        if len(v) != n:
            raise ValueError(f"Length mismatch for model '{k}': got {len(v)} vs y_true {n}")

    # Aggregate rank per sample across models to define shared bins
    ranks = [pd.Series(v).rank(method="average", pct=True).to_numpy() for v in scores.values()]
    mean_rank = np.mean(np.column_stack(ranks), axis=1)

    # Quantile bins on the aggregated rank
    if bin_var == "pred":
        bins = pd.qcut(mean_rank, q=n_bins, labels=False, duplicates="drop")
    elif bin_var == "true":
        bins = pd.qcut(y_true, q=n_bins, labels=False, duplicates="drop")

    # Build a working frame
    df = pd.DataFrame({"bin": bins, "y_true": y_true})
    for name, v in scores.items():
        df[name] = v

    # Summarize into long format
    rows = []
    for b, g in df.groupby("bin"):
        mean_true = g["y_true"].mean()
        cnt = len(g)
        for name in scores.keys():
            rows.append(
                {
                    "bin": int(b),
                    "model": name,
                    "mean_true": float(mean_true),
                    "mean_pred": float(g[name].mean()),
                    "count": int(cnt),
                }
            )
    return pd.DataFrame(rows).sort_values(["model", "bin"]).reset_index(drop=True)


def uplift_curve(u_true: np.ndarray, scores: np.ndarray):
    """Uplift curve computation.

    Build uplift curve by sorting by predicted scores (descending) and
    accumulating the true uplift. Returns fractions, normalized cumulative uplift, AUUC.
    """
    order = np.argsort(scores)[::-1]
    u_sorted = u_true[order]
    n = len(u_sorted)
    frac = np.arange(1, n + 1) / n
    cum_u = np.cumsum(u_sorted)
    total_u = np.sum(u_true)

    # Normalize to show share of total uplift captured (final value ~1 if total uplift > 0)
    if np.isclose(total_u, 0.0):
        y = cum_u  # fallback (no normalization possible)
        auuc = np.trapezoid(y, frac)
    else:
        y = cum_u / total_u
        auuc = np.trapezoid(y, frac)

    return frac, y, auuc
