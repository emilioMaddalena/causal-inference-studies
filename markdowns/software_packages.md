# Software packages

---

### DoWhy

[DoWhy](https://github.com/py-why/dowhy) is a python package developed by Microsoft. With it, you can:

- **Define causal graphs**: create DAGs, stating your assumptions. DoWhy does not perform any causal discovery, i.e., no graph learning from data.
- **Perform identification**: given a DAG and a list of observed variables (but no data), answer the question "can I, and if yes how, compute a causal effect?".
- **Estimate effects**: In case identification was successful, use data and a method (aka a model) to learn a causal link between treatment and outcome.
- **Attempt refutation**: Verify the robustness of your conclusions by performing sanity checks on it. 

---