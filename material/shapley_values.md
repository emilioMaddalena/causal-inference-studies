# **Shapley values**

---

### Introduction

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

At this point we should ask ourselves:

- How does this method work? 
- What properties does it have?
- What are its limitations?
- Are these contributions linked to causal effects?

Let's answer them one by one.

---

## How does the method work?

The method is grounded in game theory 🎲 and statistics 📊.

It regards $X$ and $f(X)$ as random variables, and computes the baseline $\phi_0$ as the expected value 

$$\phi_0 = E[f(X)]$$

whereas each individual feature contribution $\phi_i$ is given by 

$$\phi_i​=\sum_{S⊆N∖{i}} \frac{​\vert S\vert! \, (\vert N \vert− \vert S \vert−1)!}{\vert N \vert!} \, \Big(f(S∪\{i\})−f(S)\Big)$$

The formula above looks intimidating, but it's actually *a simple weighted sum*. For any so called coalition $S$, the first terms weights its importance, and the second term is the difference in function values when the feature $X_i$ is included vs when it's not included.

**So it's a simple delta!** computed and weighted across all possibles combinations of features. 

!!! example 

    You have the following values $X_1 = 10$, $X_2 = 20$, $X_3 = 30$. Here are all coallitions for $i=1$

    | $S$             | $f(S)$         | $S \cup \{i\}$ | $f(S \cup \{i\})$
    |-----------------|--------------|-------|--------|
    | [ $\emptyset$ ] | $f(\,\cdot\,,\,\cdot\,,\,\cdot\,)$     | [$1$]   | $f(10,\,\cdot\,,\,\cdot\,)$ |   
    | [ $2$ ] | $f(\,\cdot\,,20,\,\cdot\,)$     | [$1$,$2$]   | $f(10,20,\,\cdot\,)$ |   
    | [ $3$ ] | $f(\,\cdot\,,\,\cdot\,,30)$     | [$1$,$3$]   | $f(10,\,\cdot\,,30)$ |   
    | [ $2,3$ ] | $f(\,\cdot\,,20,30)$     | [$1$,$2$,$3$]   | $f(10,20,30)$ |   

    So a coallition $S$ can be thought of as the set of players active in the game.

But what does $f(\,\cdot\,,20,\,\cdot\,)$ even mean? How can we make that evaluate to a scalar in a sensible way?

Well, there are multiple ways of doing that and, up to this date, people debate what the best thing to do is. Next, we explore some of the possibilities.
