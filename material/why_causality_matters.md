# **Why causality matters**

<a id="TLDR-why-causality-matters-1"></a>
!!! tip "TL;DR"
    Because it is useful in many areas: economics, medicine, marketing, just to name a few.

Causal analysis helps us answer questions such as:

- 🏥 Does this new drug reduce recovery time compared to the standard treatment?

- 🏥 What is the effect of smoking on the likelihood of developing lung cancer?

- 📊 Does raising the minimum wage reduce employment?

- 📊 What is the impact of a universal basic income on labor market participation?

- 🧠 Do smaller class sizes cause better student outcomes?

- 🧠 Would online learning lead to worse performance than in-person instruction?

- 📈 Does offering a discount increase customer purchases?

- 📈 Does personalized advertising lead to higher conversion rates?

Not every questions is a valid causal question though. Check [this page](causal_questions.md) if you want to understand the subtleties aroud it.

<a id="TLDR-why-causality-matters-2"></a>
!!! tip "TL;DR"
    Because, once established, causal relationships generalizes well.

Because they control for confounders and rely on plenty of structure and tests, causal models are considered **more robust than general statistical or ML models**. 

For example, regulatory bodies require pharmaceutical companies to present causal proofs (via clinical trials) that new drugs indeed have the intended effect on patients.

This is so especially because causal models differentiate between variables that are targets/outputs/effects, versus the ones that are inputs/treatments, and the ones that are confounders. 

<a id="TLDR-why-causality-matters-3"></a>
!!! tip "TL;DR"
    :radioactive_sign: Using every possible covariate can be a bad idea sometimes. :radioactive_sign:

    Causal analysis tools are needed to help you select the right regression variables.

Say you want to study how a variable $X$ affects a quantity of interest $Y$, and you've also collected a number of other signals $Z_i$.

If you feed each and every variable to an ML model (think a large neural network), optimizing its weights, and calling it a day you might:

- Find a connection between $X$ and $Y$, when there is none.
- Think $X$ really impacts $Y$, when actually it is $Y$ that causes $X$.
- More in general, arrive at a wrong measure of how much $X$ influences $Y$. 
  
Causal analysis also helps us understand which $Z_i$ variables **should not be included** in the model if we really want to understand how $X$ impacts $Y$.

Different notions of impact are discussed [on this page](causal_effects.md).
