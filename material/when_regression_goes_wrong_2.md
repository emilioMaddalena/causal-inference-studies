# **When regression goes wrong 2**

!!! note "Intro"
    After going through the [coffee and paper sales](when_regression_goes_wrong.md) pickle, you've learned your lesson: never miss an important variable! Or, more explicitly...

    <div style="text-align:center;">
    *Models should have access to as many variables as possible, and ML will figure out their true relationship!*
    </div>

    Right? Well... Not so fast!

You are asked to study some new dataset, composed of the following variables:

- **Education $E$**: how many years in total different people studies
  
- **Wage $W$:** how much they make per year
  
- **Investment $I$:** how much they have invested in any type of financial instrument

And people want to know: *if you study more, will get a better salary in the future?*

Here's what the data tells you:

<div style="text-align:center;">
  <img src="../imgs/edu_wage_invest_1.png" alt="Fork" width="70%" />
</div>

All variables seem to be well behaved, and you can see clear positive association between any two of them. ✅

Let's fit a model to see if we can measure the strength of these relationships. And, just to be on the safe side, you do it using **Bayesian statistics**, to see the true level of uncertainty around your estimates.

You define the following model

$$
\begin{aligned}
W &= \alpha + \beta_E \, E  + \beta_I \, I 
\end{aligned}
$$

and the priors $\alpha \sim N(0,10)$, $\beta_E \sim N(0,10)$ and $\beta_I \sim N(0,10)$, which can lead to both negative or positive final values for those coefficients. We don't want any prior bias!





