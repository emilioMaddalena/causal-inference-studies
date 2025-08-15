# **Association vs causation**

!!! tip "TL;DR"
    Statistical association (including correlation) does not imply causation.

Statistical correlation between variables is very common and easy to find[^1]. Real and solid causation patterns are way harder. That's because **correlation can be induced by other phenomena apart from causation**, and we tend to get confused by it.

Consider this. Chocolate consumption of countries is highly correlated with the number of Nobel Prize Laureates they have. Which of the following conclusions should one draw from such association?

1. Chocolate makes you smarter, leading to a higher count of Nobel prizes.
2. People like to celebrate the winning of a Nobel prize by eating loads of chocolate.
3. Maybe the two above are true.
4. In wealthy countries people tend to eat more chocolate. Also, they tend to have better education, leading to more Nobel prizes.

All those, and many more, could be the source of the observed association. :chocolate_bar:

!!! tip "TL;DR"
    Causation involves *intervening* on a variable $T$ to affect the distribution of another variable $Y$.

We know flipping a light switch on will make the room get brighter. That's causation in action.

If we formalize this using the language of statistics, flipping the switch becomes a random variable, and it getting brighter too. That allows for non-deterministic mechanisms to be modeled, which is very useful: flipping the switch will probably turn the lights on, but maybe because of poor electrical contact they won't.

Using the so-called expected outcomes framework, a causal effect exists if

$$E[Y(T=0)] \neq E[Y(T=1)]$$

where $T=0$ represent the switch being OFF, and $T=1$ the switch being ON.

[^1]: Butter consumption is highly correlated with wind power generation! [Check it out](https://www.tylervigen.com/spurious/correlation/2205_butter-consumption_correlates-with_wind-power-generated-in-united-states). This whole website is dedicated to spurious correlations.