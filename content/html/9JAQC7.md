# Simulating Quantum Computation by Contracting Tensor Networks by Markov, Shi

[https://www.doi.org/10.1137/050644756](https://www.doi.org/10.1137/050644756)

```bibtex
@article{contractionComplexity2008,
author = {Igor L. Markov and Yaoyun Shi},
doi = {10.1137/050644756},
issn = {1095-7111},
journaltitle = {SIAM Journal on Computing},
month = {January},
number = {3},
pages = {963--981},
publisher = {Society for Industrial \& Applied Mathematics (SIAM)},
title = {Simulating Quantum Computation by Contracting Tensor Networks},
volume = {38},
year = {2008},
}
```
* page 10 : [contraction complexity]({{< base >}}html/LlWzhg) -- Definition 4.1. The contraction of an edge e removes e and replaces its end vertices (or vertex) with a single vertex. A contraction ordering π is an ordering of all the edges of G, π(1), π(2), . . ., π(|E(G)|). The complexity of π is the maximum degree of a merged vertex during the contraction process. The contraction complexity of G, denoted by cc(G), is the minimum complexity of a contraction ordering.
* page 10 : [contraction complexity]({{< base >}}html/LlWzhg) upper bounds [maximum degree]({{< base >}}html/UyQ5yM) by a linear function -- $cc(G) \ge \Delta(G) - 1$
* page 11 : [contraction complexity]({{< base >}}html/LlWzhg) upper bounds [treewidth]({{< base >}}html/5Q7fuR) by a linear function -- Proposition 4.2. ... $cc(G)=tw(G^*)$ ... Lemma 4.4. $(tw(G) - 1)/2 \le tw(G^*) \le \Delta(G)(tw(G) + 1) - 1.$
* page 11 : [degree treewidth]({{< base >}}html/nCWUh3) upper bounds [contraction complexity]({{< base >}}html/LlWzhg) by a polynomial function -- Proposition 4.2. ... $cc(G)=tw(G^*)$ ... Lemma 4.4. $(tw(G) - 1)/2 \le tw(G^*) \le \Delta(G)(tw(G) + 1) - 1.$