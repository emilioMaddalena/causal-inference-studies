The potential outcomes (PO) model (aka Rubin Causal Model) was proposed by [Donald Rubin](https://en.wikipedia.org/wiki/Donald_Rubin), a famous psychologist/statistician.

There is a group of people sitting at a crossroads point, a bifurcation. What happens to each of them is captured by the $Y_i$ variables. Every person could either take the left path ($T=0$) or go right ($T=1$), and that'd lead them to the outcomes $Y_i(0)$ or $Y_i(1)$. 

- Person $7$ goes left and you measure their outcome $Y_7 = Y_7(0)$
- But what would have happened if they had gone right? 
- Sadly, you will *never measure both* $Y_7(0)$ and $Y_7(1)$[^1]...
- Can you maybe say something about $Y(0)$, i.e. what happens *across individuals* if they take the left path?
- Maybe, if enough data is captured, you could estimate $E[Y(0)]$?
- On average, is it better to go left or right?
- Can you put a number to $E[Y(0) - Y(1)]$?

!!! tip "TL;DR"
    The PO approach is all about measuring **what happened** $Y$, and then inferring **what could have been**, $Y(0)$ and $Y(1)$.

Of course, for every individual, the value $Y_i$ will either match $Y_i(0)$ or $Y_i(1)$, but you'll never have the complete picture. One of the two outcomes will be missing. We refer to the missing one as the *counterfactual* outcome.

One key concept here is the distinction between a potential outcome $Y(1)$ and conditioning on a treatment $Y|T=1$. The difference is illustrated by the diagram below

<div style="text-align:center;">
  <img src="../imgs/PO.png" alt="po" width="40%" style="display:inline-block; margin-right:1%;" />
</div>

Conditioning $Y|T=1$ limits your dataset to those points where the units had $T=1$. On the other hand, **the quantity $Y(1)$ is a thought experiment **where all units received the treatment $T=1$. 

Because your dataset $Y$ contains some parts of the puzzle, you can estimate lots of interesting quantities under the right supporting assumptions.

!!! tip "TL;DR"
    Identification is the process of inferring things about $Y(0)$ and/or $Y(1)$ from the observational data you have, $Y$.

The average treatment effect (ATE) is defined as the expected difference 

$$\tau = E[Y(1) - Y(0)]$$

This is what you want to know when you ask yourself "*does eating one apple a day really keep the doctor away???*"

Here's one simple idea: how about computing the average outcome among apple lovers $E[Y|T=1]$ and subtracting that from the apple haters $E[Y|T=0]$ we have in our sample set? That should be similar to $\tau$, right?

Well, it turns out this can sometimes go very very wrong...

If you **miss important variables in your analysis**, those could *confound* your groups and mess-up your results! Imagine that, by chance, all smokers ended up in your $T=0$ group, whereas all the young athletes loved fruits and had $T=1$. In that case you'll certainly conclude the apples kept the doctor away.

You have two ways out: either balancing your groups[^2] or taking the additional variables (smoking, doing sports, etc) explicitly into account. The more general principle at play here, what guarantees we can perform causal inference, is the one that follows.

!!! tip 
    Exchangeability $Y(0), Y(1) \perp T$ and Conditional Exchangeability $Y(0), Y(1) \perp T \, | \, X$ are key to identification.

[^1]: That's called *the fundamental problem of causal inference*.
[^2]: [Randomized controlled trials](https://en.wikipedia.org/wiki/Randomized_controlled_trial) (RCTs) do exactly that.