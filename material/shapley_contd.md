# **Shapley cont'd**

---

### Shapley values vs. causal effects

Shapley values explain the effects of $X_1, \dots, X_n$ on $Y$, but they require you to specify values for all of the features. In other words, **they explain your model $f$ around a fixed point in the domain**. The fact that Shapley computations average out multiple $X$ values via the expectation doesn't change the fact those are always contrasted to the user-given fixed point.

Causal effects, on the other hand, capture the influence of $X$ on $Y$ **across the whole domain** and do not require pre-specifying a set of feature values. Indeed, take the ATE expression for a binary treatment $\tau = \text{E}[Y(0) - Y(1)]$. Assuming the treatment $X$ is binary, it consider both values and contrasts both $Y$ distributions.

To better understand what's going on here, let's go back go a very simple linear example.

!!! example 

    Take $Y = f(X) = 5 X_1 + 3 X_2$.

    If you were to analyze $f$ around $X_1 = 1$, $X_2 = 10$, you'd get the Shapley values $\phi_1 = 5$ and $\phi_2 = 30$, assuming your baseline is $\phi_0 = 0$, which would happen if both features had distributions centered around zero. Now if you take $X_1 = 2$, $X_2 = 20$ you get $\phi_1 = 10$ and $\phi_2 = 60$, and so on...

    **Shapley values vary and can be directly tied to the output**... you could say they share the same measurement units! 📏

    What's the causal effect of $X_1$ on $Y$? Well, under unconfoundedness, it's... $5$. And the causal effect of $X_2$ on $Y$ is... $3$. If we're talking ATEs, those don't vary across the domain[^1].

    The causal effect is not a measure of direct contribution to $Y$, but of the features derivative.


---

## Shapley properties

How do Shapley values behave, though? What properties can we expect them to have?

Here's a summary:

| Property | Explanation | Math | 
|--|--|--|
| Efficiency | The sum of all Shapley values equals the function output | $\sum \phi_i = f(x)$ |
| Symmetry | Features with the same contributions get equal Shapley values | $f(S \cup \{i\}) = f(S \cup \{j\}), \forall S \implies \phi_i = \phi_j$
| Null player | Features that don't contribute have zero Shapley values | $f(S \cup \{i\}) = f(S), \forall S \implies \phi_i = 0$|
| Linearity | Shapley values respect linearity of $f$ | $f = \alpha g + \beta h \implies \phi_{f,i} = \alpha\phi_{g,i} + \beta\phi_{h,i}$|

Additional properties are listed in [this paper](https://proceedings.mlr.press/v119/sundararajan20b/sundararajan20b.pdf) and on the following [wikipedia page](https://en.wikipedia.org/wiki/Shapley_value).

What is important to keep in mind is that some Shapley versions do not satisfy the extended set of properties. Still, those are supposed to help you build an intuition around how they behave and how they should be interpreted in practice.


[^1]: As opposed to ATEs, CATEs do vary depending on auxiliary (context) variables. Still, the derivative interpretation still holds in that case.

