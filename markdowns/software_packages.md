# Software packages

---

### DoWhy

[DoWhy](https://github.com/py-why/dowhy) is developed by Microsoft. With it, you can:

- **Define causal graphs**: create DAGs, stating your assumptions. DoWhy does not perform any causal discovery, i.e., no graph learning from data.
- **Perform identification**: given a DAG and a list of observed variables (but no data), answer the question "can I, and if yes how, compute a causal effect?".
- **Estimate effects**: In case identification was successful, use data and a method (aka a model) to learn a causal link between treatment and outcome.
- **Attempt refutation**: Verify the robustness of your conclusions by performing sanity checks on it. 

---

### causal-learn

[causal-learn](https://github.com/py-why/causal-learn) can be used to learn DAGs from data (and assumptions). It implements various related learning methods (constraint-based, score-based, permutation-based, etc), and provides utilities to carry out independence tests and evaluate learned graphs.

---

### networkx 

[networkx](https://github.com/networkx/networkx) is the go-to python package for graph creation and manipulation. Also, it is not limited to DAGs. With networkx, you can analyze graphs by computing centrality measures, and carrying out structural and connectivity analyses for example.
