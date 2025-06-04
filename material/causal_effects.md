# **Causal effects**
---

> TL;DR
> 
> The fundamental problem of Causal Inference is that we can't change the past.

---

You feel unwell, so you take some meds and go to bed...

Next day you wake up just fine. Was it thanks to the meds or did you body just recover by itself? 

Well, we will never know!

The so-called fundamental problem of causal inference is that **never will we be able to measure causal effects on an individual basis**. And that's because we can't go back in time, intervene (not taking the meds) and verify what happened to be 100% the observed outcome was due to the intervetion.

---

> TL;DR
> 
> TBW.

---

To be covered:
- Individual Treatment Effect (ITE)
- Total Effect (TE)
- Natural Direct Effect (NDE)
- Natural Indirect Effect (NIE)
- Controlled Direct Effect (CDE)

---

| Acronym | Effect Name | Definition | Interpretation |
|:--------|:-----------:|:----------:|:--------------:|
| ATE | Average Treatment Effect | $E[Y(1)−Y(0)]E[Y(1)−Y(0)]$ | Effect on a random individual in the population |
| ITE | Individual Treatment Effect | $Y_i​(1)−Yi_​(0)$ | Effect on a random individual in the population |
| CATE | Conditional Average Treatment Effect |	$Y_i​(1)−Yi_​(0)$ | Effect on a random individual in the population |



