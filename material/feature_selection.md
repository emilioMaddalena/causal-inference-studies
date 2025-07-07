# **Feature selection**

<a id="TLDR-the-good-and-the-bad"></a>
!!! tip "TL;DR"
    Not every variable should be included in your models.

Modern machine learning advocates for including all you can in your model, trying to achieve the lowest possible (test) error.

This is a fair strategy if you are aiming at **capturing patterns and predicting labels**. 

If, however, your goals are more causal oriented (see the [causal questions page](causal_questions.md)), for instance:

- Study *the main drivers* of your output variable
- *Design a policy* based on your model to influence your output
- Understand *what would have been* if one of your variables had taken a different value

then the ML approach can fall short of delivering a good answer. 

In contrast to confounders, which should be controlled for, there are also other variables that harm our estimates if included in our models.