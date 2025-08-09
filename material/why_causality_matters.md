# **Why causality matters**

<a id="TLDR-why-causality-matters-1"></a>
!!! tip "TL;DR"
    Because it is useful in many areas: economics, medicine, marketing, just to name a few.

Causal analysis helps us answer questions like:

- 🏥 What is the effect of smoking on the likelihood of developing lung cancer?

- 📊 Does raising the minimum wage reduce employment?

- 🧠 Do smaller class sizes cause better student outcomes?

- 📈 Does personalized advertising lead to higher conversion rates?

So, in essence, causal inference helps us understand and predict what will happen if we intervene on some variable.

<a id="TLDR-why-causality-matters-2"></a>
!!! tip "TL;DR"
    Because causal models succeed 💪 when non-causal models fail ☹️.

**If your goal is to change variable $Y$ by acting on variable $X$, you need causal analysis**.

Throwing every variable you have at your model can lead to serious interpretability issues, and make you believe you can drive $Y$ when you actually can't. Sometimes it can reverse signs in a linear model, suggesting the link between a given $X$ and a $Y$ is positive when it's actually negative...[^1] 

Causal inference tool help us build models that generalize well and with which we can make robust *interventions*[^2].

[^1]: There are tasks in which causal analysis is not required, of course. Some of those are discussed in the non-causal questions page.

[^2]: Regulatory bodies for example require pharmaceutical companies to present causal proofs (via clinical trials) that new drugs indeed have the intended effect on patients. Merely training an ML model to show a positive association isn't enough! :pill:
