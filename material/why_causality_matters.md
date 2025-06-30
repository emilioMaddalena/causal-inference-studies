# **Why causality matters**

<a id="TLDR-why-causality-matters-1"></a>
!!! tip "TL;DR"
    Because it is useful in many areas: economics, medicine, marketing, just to name a few.

Causal analysis helps us answer questions like:

- 🏥 What is the effect of smoking on the likelihood of developing lung cancer?

- 📊 Does raising the minimum wage reduce employment?

- 🧠 Do smaller class sizes cause better student outcomes?

- 📈 Does personalized advertising lead to higher conversion rates?

So, in essence, causal inference helps us understand and predict what will happen if we **intervene on some variable**.

<a id="TLDR-why-causality-matters-2"></a>
!!! tip "TL;DR"
    Because, once established, causal relationships generalize well.

Because they are grounded in additional assumptions and tests, causal models are considered **more robust** than general statistical or even machine learning models. 

Regulatory bodies for example require pharmaceutical companies to present causal proofs (via clinical trials) that new drugs indeed have the intended effect on patients. Merely training an ML model to show a positive association isn't enough! :pill:

In the world of CI, one needs to understand if it's even possible (or not!) to derive the effect of interest, and what variables should be included if the answer is positive. All of this happens before running a single gradient descent step!

<a id="TLDR-why-causality-matters-3"></a>
!!! tip "TL;DR"
    Because using every possible covariate can be a bad idea sometimes. :radioactive_sign:

    Causal tools are needed to help you select the right regression variables.

Say you want to study how $X$ affects $Y$, and you've also collected a number of $Z_i$.

If you feed $X$ and $Z$ to a model and blindly optimize its MSE wrt to $Y$, you might...

- Find a connection between $X$ and $Y$ when there is none.
- Think $X$ really impacts $Y$, when actually it is $Y$ that causes $X$.
- More in general, arrive at a wrong measure of how much $X$ influences $Y$. 
  
Instead of using all $Z_i$ or ignoring all $Z_i$, causal analysis helps you understand which should stay and which should go, and **why**!

See [this example](confounders.md#TLDR-confounders-are-bad).
