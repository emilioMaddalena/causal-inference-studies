# **When regression goes wrong**

You're a data scientist at an office supply company (maybe Dunder Mifflin 📎) and are given this dataset by your manager

<div style="text-align:center;">
  <img src="../imgs/cc_os.png" alt="Fork" width="50%" />
</div>

Clearly **both variables are linked**, and there's a neat linear in the plot. You open a jupyter notebook and fit a linear model using [statsmodels](https://www.statsmodels.org/stable/index.html) to even investigate the p-values of the coefficients that were estimated. The table you get reassures you: the IC parameter is not only linear as expected, but also has a very low p-value[^1]!

<div style="text-align:center;">
  <img src="../imgs/cc_os_params.png" alt="Fork" width="60%" />
</div>

There's just one thing that bothers you... Nobody has told you yet what the variables really are! 🤔🤔

You go turn some rocks and find out CC stands for *coffee consumption* and OS, for office supply sales. What's more concerning, your boss is thinking of sending clients complimentary coffee bags in the hopes of boosting your sales.

<div style="text-align:center;">
  <img src="../imgs/coffee_consumption_office_supplies.png" alt="Fork" width="50%" />
</div>

Now that got you worried because if the strategy fails, people will think your analyses are really flawed, you can't even get a linear model right!

After some careful thinking, you realize maybe this link between coffee consumption and sales can be explained by **company size**, which you were missing in your model. Clients with a larger headcount also buy more from you. But **offering them free coffee won't really affect their purchasing patterns**...

After finding the new column you wanted and fitting a new model, voilà, you arrive at

<div style="text-align:center;">
  <img src="../imgs/coffee_companysize_sales.png" alt="Fork" width="60%" />
</div>

showing that coffee consumption has essentially no effect on sales (the confidence interval goes between $-0.026$ and $0.019$ and the p-value is very high, $0.775$). On the other hand, company size explains all the sales variation (positive coefficient of $0.5022$ and p-value of $<0.001$).

You manage to convince your boss to drop the coffee distribution, the day is saved. 🌟



[^1]: This indicates that the association you've found was not due to mere chance.

