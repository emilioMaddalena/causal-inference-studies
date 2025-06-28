# **Confounders**

!!! tip "TL;DR"
    A confounder is a variable that is not the treatment, nor the effect, but that can affect the association between the two.

You have some data on the monthly ice cream sales in Brazil and the number of shark attacks on a costal region. Both variables are highly correlated as shown below.

<div style="text-align:center;">
  <img src="../imgs/confounders1.png" alt="Fork" width="50%" />
</div>

One could propose the following DAG to try to explain the phenomenon.

<div style="text-align:center;">
  <img src="../imgs/confounders2.png" alt="Fork" width="50%" />
</div>

But perhaps the one below, with season influencing both blue variables, would be a more sensible structure.

<div style="text-align:center;">
  <img src="../imgs/confounders3.png" alt="Fork" width="50%" />
</div>


**The season node is a confounder** as it affects both main variables of interest. In this example, it being summer drives up both ice cream sales and shark incident, giving the impression there is a causal link between the two.

!!! tip "TL;DR"
    Confounders are bad: they can lead you to spurious conclusions if you ignore them. 

If you fit a linear model to predict shark attacks from ice cream sales, you get a very nice graph (see [notebook](../notebooks/sharks_and_ice_creams.ipynb))

<div style="text-align:center;">
  <img src="../imgs/ice_cream_no_temp.png" alt="ice cream no temp" width="50%" style="display:inline-block; margin-right:1%;" />
</div>

Not only that, the linear coefficient of the predictor (ice cream sales) even has a very low p-value

<div style="text-align:center;">
  <img src="../imgs/ice_cream_no_temp_p_vals.png" alt="ice cream no temp" width="60%" style="display:inline-block; margin-right:1%;" />
</div>

So it's all statistically sound, right? Time to use of this model to make some great decisions!

---

Well, if you had included temperature, you'd see a very different 

<div style="text-align:center;">
  <img src="../imgs/ice_cream_temp.png" alt="ice cream no temp" width="50%" style="display:inline-block; margin-right:1%;" />
</div>

And the p-values of ice-cream are now very high

<div style="text-align:center;">
  <img src="../imgs/ice_cream_temp_p_vals.png" alt="ice cream no temp" width="60%" style="display:inline-block; margin-right:1%;" />
</div>

Conclusion: TBW...

!!! tip "TL;DR"
    The three elemental confounds are: the <strong>fork</strong>, the <strong>pipe</strong>, and the <strong>collider</strong>.

There are three main types of confounding structures, which are defined by 3-node diagrams. Any more complex DAG can be analyzed based on these.

<div style="text-align:center;">
  <img src="../imgs/confounders4.png" alt="Fork" width="32%" style="display:inline-block; margin-right:1%;" />
  <img src="../imgs/confounders5.png" alt="Pipe" width="32%" style="display:inline-block; margin-right:1%;" />
  <img src="../imgs/confounders6.png" alt="Collider" width="32%" style="display:inline-block;" />
</div>

At first sight, the collider seems inoffensive as there are no arrows going from $Z$ to $X$ or $Y$, so how could it bias our analysis?

Well, causal effects respect the arrow directions, but statistical association doesn't. It can flow against them.

!!! tip "TL;DR"
    :sparkles::sparkles::sparkles: Treatment randomization is magical: it makes all confounding go away! :sparkles::sparkles::sparkles: 

If you were to randomly give out ice cream to people, regardless of the season, you would see the association between ice cream and shark attacks disappear.

With the DAG in mind, randomization would **cut the arrow** that connects season and ice cream, disqualifying season as a confounder.

This is the beauty of randomized controlled trials (RCTs), widely employed in medical studies. By randomly assigning patients to the treatment or control group, you break all confounding. No wonder why RCTs are regarded as a gold standard in that field.

!!! tip "TL;DR"
    Under no confounding, causal inference becomes trivial.

Say you want to estimate the average extra hours of sleep you get if you take some miraculous new medicine

$$\text{ATE} = E[Y(1) - Y(0)]$$

You run an experiment and, if $T$ was randomized, the causal effect is as simple as

$$\text{ATE} = E[Y \, | \, T=1] - E[Y \, | \, T=0]$$

that is, averaging the sleep hours $Y$ among all people who got the med, and subtracting the average sleep hours $Y$ for all who didn't take the med.

N.B. Of course you'd still have to check if the final number is reliable or not (was your sample too small?). The estimator isn't biased, but variance can still hit you hard. 