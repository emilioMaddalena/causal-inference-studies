# **Shapley values**

Shapley values were originally proposed in the 50s as a way of distributing a total prize among a series of players participating in a game. If you imagine **the prize is the model output $y$**, and **the players are the individual features $x_i$**, you can re-use the same theory to better understand ML models!

Picture this. Your model produced an output $f(x)$, and you want to understand why. Shapley values decompose your prediction into parts

$$f(x) = \phi_0 + \sum_{i} \phi_i$$

where each $\phi_i$ summarizes the contribution of feature $x_i$ to the output! and $\phi_0$ is a baseline constant value.

!!! example 
    
    You have a model to predict someone's expected yearly salary and want to explain why for person $X$, the output was $ 89'000. Shapley could then give you a decomposition such as

    | Feature | Shapley value |
    |---------|--------------|
    | $\phi_0$ | 45'000 |
    | age = 42 | +33'000 |
    | education = MSc | +4'000 |
    | eyes = brown | -1'000 |
    | fav cheese = gouda | -3'000 |
    | children = 3 | +11'000 |
    | **Total** 💰 | 89'000 |

    where $\phi_0$ is the average salary predicted by the model.

    That's kind of cool, right? **Even if your model isn't linear**, shapley gives you the **isolated contributions of each feature** to the predicted value. 