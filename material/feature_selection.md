# **Feature selection**

<a id="TLDR-the-good-and-the-bad"></a>
!!! tip "TL;DR"
    To estimate causal effects well, you need to carefully select your features/predictors/regressors.

Modern machine learning advocates for including all you can in your model, trying to achieve the lowest possible (test) error.

This is a fair strategy if you are aiming at **capturing patterns and predicting labels**. 

If, however, your goals are more causal oriented (see the [causal questions page](causal_questions.md)), for instance:

- Study *the main drivers* of your output variable
- *Design a policy* based on your model to influence your output
- Understand *what would have been* if one of your variables had taken a different value

then the ML approach can fall short of delivering a good answer. 

<a id="TLDR-You-need-to-include-confounders"></a>
!!! tip "TL;DR"
    Some variables must be included. For example, confounders.

<a id="TLDR-some-variables-are-bad"></a>
!!! tip "TL;DR"
    Some variables must not be included. Including them will bias your model.

<a id="TLDR-some-variables-are-neutral"></a>
!!! tip "TL;DR"
    Some variables are neutral, including them or not doesn't make a difference.

<a id="TLDR-the-backdoor-criterion-tells-us-which-variables-to-include"></a>
!!! tip "TL;DR"
    The backdoor criterion tells us which variables to include in our models.

<a id="TLDR-adjustment-sets-are-equal"></a>
!!! tip "TL;DR"
    All adjustment sets are equal, but some are more equal than others.



