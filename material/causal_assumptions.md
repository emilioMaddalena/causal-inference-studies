# **Causal assumptions**
---

> TL;DR
> 
> Establishing causal relationships requires making various assumptions.

---

Causal inference does not rely purely on data and statistics. It requires more assumptions for causal relationships to be established.


[DAGs](dags.md) are a visual way of expressing our beliefs about how different quantities influence each other.


As it turns out, DAGs are not enough. **Even with infinite data** and a DAGs in place, **some causal relationships cannot be estimated**.

---

> TL;DR
> 
> **Exchangeability**: assuming if the control and treatment groups were swapped, the results would have been the same.

---

Formally, exchangeability reads

$$Y(0) \perp T, \quad Y(1) \perp T$$

where $T$ is the treatment assignment, $Y(0)$ is the outcome for when not receiving the treatment, and $Y(1)$ is the outcome when receiving the treatment.

A less strict version of this assumption would be

$$E[ Y(1) \, | \, T = 0 ] = E[ Y(1) \, | \, T = 1 ]$$

which asks for the expected value of having received the treatment (a counterfactual in the left-hand side case) to be the same under being assigned to the control group ($T=0$) or the treatment group ($T=1$).