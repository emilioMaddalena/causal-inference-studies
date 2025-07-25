# **Propensity scores**

!!! tip "TL;DR"
    Propensity scores are likelihoods. The likelihood of a certain type of unit receiving the treatment.

Experiments are usually design balancing groups of treated $T=1$ vs control people $T=0$. And making sure that, if our population has some important features $X$, those will be **equally represented in both groups**.

Imagine testing the effectiveness of a new dietary supplement. Given some characteristic $X = \text{vegan}$, you'd want to see roughly the same number of these individuals in the treated and untreated groups. 

In observational studies, groups are not balanced and propensity scores measure that unbalance. Formally,

$$e(x) \triangleq P(T = 1 | X = x)$$

If $e(x) = 0.5$ for all $x$, this means the treatment is actually independent of $x$ and we've truly randomized it, guaranteeing no confounding!

!!! tip "TL;DR"
    Instead of controlling for $X$, you can control for $e(X)$ and that is great.


!!! tip "TL;DR"
    Inverse-probability weighting (IPW) is a method that uses propensity scores to estimate causal effects.




