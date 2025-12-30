# **Randomized data: why and how**

!!! tip "TL;DR"
    Randomized data is gold. When you have it, estimating ATEs becomes amounts to a difference in means.

When we say "randomized", we mean our dataset is free of bias. 

Mathematically, using the [Potential Outcomes](potential_outcomes.md) formalism, we require $Y(0), Y(1) \perp T$, which is known as the *Ignorability* or *Exchangeability* assumption. Essentially, you can ignore how units ended up in the treatment or control groups, because *the assignment was random*. Put otherwise, your results would have been the same (statistically), had you swapped units. 

Why is that so important, you ask? Well, because under that assumption 

$$
\begin{align}
E[Y(1) - Y(0)] &= E[Y(1)] - E[Y(0)] \\[5pt]
&= E[Y(1) | T=1] - E[Y(0) | T=0] \\[5pt]
&= E[Y | T=1] - E[Y | T=0]
\end{align}
$$

or, in plain English, the ATE is a simple difference between the average outcome in the treated and control groups.




!!! tip "TL;DR"
    A/B test and RCTs, when done right, give you randomized data. And Randomized data is gold.

Directed acyclic graphs (DAGs) are an intuitive way of expressing your beliefs about a set of variables. 


!!! tip "TL;DR"
    Randomized


!!! tip "TL;DR"
    A/B tests are a form of randomized control trials (RCTs)and ensure no sample bias, leading to an easy estimation of average treatment effects.
    
Directed acyclic graphs (DAGs) are an intuitive way of expressing your beliefs about a set of variables. 

Resources:

https://alexdeng.github.io/causal/abintro.html

*The Relationship between Experimentation and Causal Inference*. Sean Taylor. [[video](https://www.youtube.com/watch?v=5Myw5A-ZILs)]