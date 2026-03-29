## Copilot / AI quick instructions — causal-inference-studies

Purpose & scope
- Short: docs + example notebooks for causal inference. Edit content in `material/` and helper code in `material/notebooks/`.
- Do NOT edit generated output under `site/` or change CI/workflow files without explicit human approval.
- Python: repository targets Python >= 3.12 (see `pyproject.toml`).

Canonical setup (run locally before opening a PR)

```bash
# Using standard venv
python -m venv .venv
source .venv/bin/activate
python -m pip install .

# Using uv (recommended)
uv sync --all-extras
uv run mkdocs serve
```

Quick smoke checks (run these before creating a PR)

```bash
# Lint (and optionally autofix)
uv run ruff check .
# uv run ruff check --fix .

# Run tests (if present)
uv run pytest -q

# Minimal smoke import to validate notebooks helpers
uv run python - <<'PY'
from material.notebooks.uplift_modelling_utils import data_generating_process
_ = data_generating_process(10, setting='default', seed=0)
print('smoke OK')
PY
```

Where to edit (golden paths)
- `material/` — canonical Markdown lessons and notebooks.
- `material/notebooks/` — reusable helper modules used by notebooks (preferred place for logic changes).
- `site/` — generated output. Never edit directly.

High-value files (review before editing)
- `material/notebooks/uplift_modelling_utils.py` — DGP, calibration and AUUC helpers.
- `mkdocs.yml` — site navigation and plugin configuration.
- `pyproject.toml` — dependency / Python version pin.

Edit patterns & safety
- Prefer small, localized edits. If a change is reused in multiple notebooks, update the helper module and add a small test or notebook example.
- Avoid broad refactors. If the change touches many files or is architectural, open an issue first and discuss.
- Never commit secrets, credentials, or .env files.
- Do not modify CI workflows, deployment settings, or `mkdocs.yml` without explicit human review.

Commit & PR conventions
Purpose: keep commits and PRs easy to review and trace.

- Commit message format (recommended):
  - Short summary (<= 72 chars)
  - Blank line
  - Optional longer description explaining why

  Example:
  ```
  add AUUC plotting helper

  Adds uplift_curve() helper used by notebooks and a small unit test.
  ```

- PR title templates:
  - `feat/<short-desc>` — new features
  - `fix/<short-desc>` — bug fixes
  - `docs/<page>-update` — docs or notebook content
  - `chore/<short-desc>` — maintenance

- PR body (copy this checklist into the PR):
  - Short summary (1–2 sentences)
  - Commands run to verify (e.g., `mkdocs serve`, `python -m pip install .`, `ruff .`, `pytest -q`)
  - Files changed (list or short summary)
  - Tests added/updated: yes/no
  - Risk / rollback notes (if applicable)
  - Suggested reviewers

Size & scope guidance
- Prefer PRs that are single-purpose and < 300 LOC when possible.
- If a change touches > 10 files or reworks a subsystem, open an issue first.

Automated-agent (Copilot) rules
- Automated edits must:
  - Touch <= 10 files and <= 300 LOC.
  - Include runnable verification commands and, if changing behavior, a test or smoke notebook run.
  - Never modify CI/workflow/deploy files or secrets.
- If unsure about intent or scope, create an issue and tag maintainers rather than opening a large automated PR.

Reviewers & approvals
- Docs / notebooks: tag @emilioMaddalena
- Infra / CI / deploy: request review from a maintainer and wait for explicit human approval

If in doubt
- For any change touching CI, deploy, or large parts of the site, open an issue and get consensus before implementing.
- For ambiguous edits, prefer conservative, minimal changes and state assumptions in the PR body.

Optional personality lines (keep or remove):
- "If your patch changes >10 files or touches `mkdocs.yml`, open an issue first."
- "Don’t rewrite history on shared branches — avoid force-pushes."
