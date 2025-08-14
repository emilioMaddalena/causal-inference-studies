# **DAGs 2**

!!! tip "TL;DR"
    The <strong>fork</strong>, the <strong>pipe</strong>, and the <strong>collider</strong> are three elemental building blocks of any DAG.

These are important basic structures that can be used to analyze more complex DAGs.

<div style="text-align:center;">
  <img src="../imgs/confounders4.png" alt="Fork" width="32%" style="display:inline-block; margin-right:1%;" />
  <img src="../imgs/confounders5.png" alt="Pipe" width="32%" style="display:inline-block; margin-right:1%;" />
  <img src="../imgs/confounders6.png" alt="Collider" width="32%" style="display:inline-block;" />
</div>

In the TL;DRs below, we will explore basic...

!!! tip "TL;DR"
    In a fork, conditioning on $Z$ blocks the path between $X$ and $Y$.

From the Markov factorization of the fork, we have

$$p(X,Y,Z) = p(X|Z) \; p(Z) \; p(Y|Z)$$

Now the conditional $p(X,Y | Z)$ can be written as[^1]

$$
\begin{align}
p(X,Y | Z) &= \frac{p(X,Y,Z)}{p(Z)} \\[5pt]
&= p(X|Z) \; p(Y|Z)
\end{align}
$$

which is the definition of the conditional independence $X \perp Y  \, | \, Z$.

!!! tip "TL;DR"
    In a pipe, conditioning on $Z$ blocks the path between $X$ and $Y$.

This will be similar to the fork case. We have

$$p(X,Y,Z) = p(X) \; p(Z|X) \; p(Y|Z)$$

Then[^2]

$$
\begin{align}
p(X,Y | Z) &= \frac{p(X,Y,Z)}{p(Z)} \\[5pt]
&= \frac{p(X) \; p(Z|X) \; p(Y|Z)}{p(Z)} \\[5pt]
&= \frac{p(X,Z) \; p(Y|Z)}{p(Z)} \\[5pt]
&= p(X|Z) \; p(Y|Z)
\end{align}
$$

which is the definition of the conditional independence $X \perp Y  \, | \, Z$.

!!! tip "TL;DR"
    In a collider, the path between $X$ and $Y$ **is naturally closed**.

From the Markov factorization of the fork, we have

$$p(X,Y,Z) = p(X) \; p(Y) \; p(Z|X,Y)$$

then

$$
\begin{align}
p(Y|X) &= \frac{p(X,Y)}{p(X)} \\[5pt]
&= \frac{\sum_z p(X,Y,Z)}{p(X)} \\[5pt]
&= \frac{\sum_z p(X) \; p(Y) \; p(Z|X,Y)}{p(X)} \\[5pt]
&= \frac{p(X) \, p(Y)}{p(X)} \\[5pt]
&= p(Y)
\end{align}
$$

So $p(X,Y) = p(X) \, p(Y|X) = p(X) p (Y)$, which is the definition of the independence $X \perp Y$.

[^1]: The first equality follows from the def. of the conditional probability. The second, from the Markov factorization above.
[^2]: The first equality follows from the def. of the conditional probability. The second, from the Markov factorization above. The third, from the product rule. The fourth, from the definition of the conditional probability.
