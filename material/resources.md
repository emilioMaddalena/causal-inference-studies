# Resources

### Software packages

[DoWhy](https://github.com/py-why/dowhy) is developed by Microsoft, and with it you can define causal graphs, perform identification, estimate effects, and attempt refutation. DoWhy forces you to state your causal assumptions via a DAG and rigorously go through all causal inference steps.

[causal-learn](https://github.com/py-why/causal-learn) can be used to learn DAGs from data (and assumptions). It implements various DAG learning methods (constraint-based, score-based, permutation-based, etc), and provides utilities to carry out independence tests and evaluate learned graphs.

[causalml](https://github.com/uber/causalml) is a python package for effect estimation with a focus on ML, especially tree-based methods. As opposed to `DoWhy`, it is less formal with assumptions and does not offer extensive identification and refutation tools. It is aimed at data scientists and tech firms, instead of economists.

[networkx](https://github.com/networkx/networkx) is the go-to python package for graph creation and manipulation. Also, it is not limited to DAGs. With networkx, you can analyze graphs by computing centrality measures, and carrying out structural and connectivity analyses for example.

---

### Books

- (2000) *Causality - Models, Reasoning and Inference*. J. Pearl.
- (2010) *Causal Inference - What If*. M. A. Hernán, J. M. Robins.
- (2017) *Elements of Causal Inference - Foundations and Learning Algorithms*. J. Peters, D. Janzing, B. Schölkopf.
- (2024) *Causal Inference: A Statistical Learning Approach*. S. Wager. 

---

### Videos

- (2019) *MIT Lectures on Causal Inference for Healthcare*. [[YouTube](https://www.youtube.com/watch?v=gRkUhg9Wb-I)]
- (2017) *Lectures on Causality series*, J. Peters. [[YouTube](https://www.youtube.com/watch?v=zvrcyqcN9Wo)]
- (2015) *Towards Causal Machine Learning*, B. Schölkopf. [[YouTube](https://www.youtube.com/watch?v=ooeRlw3U2zU)]
- (2021) *Machine Learning and Causal Inference*, Stanford. S. Wager. [[YouTube](https://www.youtube.com/watch?v=ZA8iOjUR8aY&list=PLxq_lXOUlvQAoWZEqhRqHNezS30lI49G-&index=5)]
  
---

### Articles, slide decks, repos

- (2009) *Causal inference in statistics: An overview*. J. Pearl
- (2019) *Causality for Machine Learning*. B. Schölkopf. [[paper](https://arxiv.org/pdf/1911.10500)]
- (2023) *Statistical Rethinking Course*, R. McElreath. [[slides](https://github.com/rmcelreath/stat_rethinking_2024), [YouTube](https://www.youtube.com/watch?v=FdnMWdICdRs&list=PLDcUM9US4XdPz-KxHM4XHt7uUVGWWVSus)]
- (2021) *Causal Inference: An overview*. A. Deng. [[repo](https://alexdeng.github.io/causal/)]
- (2022) *Causal Inference for the Brave and True*. M. Facure. [[repo](https://matheusfacure.github.io/python-causality-handbook/landing-page.html)]

