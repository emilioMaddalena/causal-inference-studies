# **Association vs causation**

!!! tip "TL;DR"
    Statistical association (including correlation) does not imply causation.

Statistical correlation between variables is very common and easy to find[^1]. Real and solid causation patterns are way harder. That's because **correlation can be induced by other phenomena apart from causation**, and we tend to get confused by it.

Consider this example :chocolate_bar::chocolate_bar::chocolate_bar:

Chocolate consumption of countries is highly correlated with the number of Nobel Prize Laureates they have. Although it's amusing to think chocolate will help you get that smarter, it's also hard to believe that is indeed the case. If you think about it harder though, which of the following conclusions should one draw from such association?

1. Chocolate makes you smarter, leading to a higher count of Nobel prizes.
2. People like to celebrate the winning of a Nobel prize by eating loads of chocolate.
3. Maybe the two above are true.
4. In wealthy countries people tend to eat more chocolate. Also, they tend to have better education, leading to more Nobel prizes.

All those, and many more, could be the source of the observed association.

!!! tip "TL;DR"
    Causation involves *intervening* on a variable $T$ to affect the distribution of another variable $Y$.

We know flipping a light switch on will make the room get brighter. That's causation in action.

The TL;DR above formalizes this notion using the language of statistics, where the flipping a switch becomes a random variable, and it getting brighter too. It also allows for non-deterministic mechanisms: flipping the switch will probably turn the lights on, but maybe because of poor electrical contact they won't.

If establishing correlation is easy, establishing causation is hard. Sometimes impossible even if you had infinite data!

But don't panic - with the right theory and the right tools, much can be accomplished :sunglasses:

[^1]: Butter consumption is highly correlated with wind power generation! [Check it out](https://www.tylervigen.com/spurious/correlation/2205_butter-consumption_correlates-with_wind-power-generated-in-united-states). This whole website is dedicated to spurious correlations.