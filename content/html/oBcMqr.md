# Parameterized complexity for iterated type partitions and modular-width by Cordasco, Gargano, Rescigno

[https://www.doi.org/10.1016/j.dam.2024.03.009](https://www.doi.org/10.1016/j.dam.2024.03.009)

```bibtex
@article{iteratedTypePartitions2024,
author = {Gennaro Cordasco and Luisa Gargano and Adele A. Rescigno},
doi = {10.1016/j.dam.2024.03.009},
issn = {0166-218X},
journaltitle = {Discrete Applied Mathematics},
pages = {100--122},
title = {Parameterized complexity for iterated type partitions and modular-width},
volume = {350},
year = {2024},
}
```
* page 3 : [iterated type partitions]({{< base >}}html/G1Cwmc) -- two nodes have the same type iff $N(v) \setminus \{u\} = N(u) \setminus \{v\}$ ... [ed. paraphrased] let $\mathcal V = \{V_1,\dots,V_t\}$ be a partition of graph vertices such that each $V_i$ is a clique or an independent set and $t$ is minimized ... we can see each element of $\mathcal V$ as a \emph{metavertex} of a new graph $H$, called \emph{type graph} of $G$ ... We say that $G$ is a \emph{prime graph} if it matches its type graph ... let $H^{(0)}=G$ and $H^{(i)}$ denote the type graph of $H^{(i-1)}$, for $i \ge 1$. Let $d$ be the smallest integer such that $H^{(d)}$ is a \emph{prime graph}. The \emph{iterated type partition} number of $G$, denoted by $\mathrm{itp}(G)$, is the number of nodes of $H^{(d)}$.
* page 3 : [neighborhood diversity]({{< base >}}html/vMs3RS) upper bounds [iterated type partitions]({{< base >}}html/G1Cwmc) by a linear function -- ... $itp(G) \le nd(G)$. Actually $itp(G)$ can be arbitrarily smaller than $nd(G)$.
* page 3 : bounded [iterated type partitions]({{< base >}}html/G1Cwmc) does not imply bounded [neighborhood diversity]({{< base >}}html/vMs3RS) -- ... $itp(G) \le nd(G)$. Actually $itp(G)$ can be arbitrarily smaller than $nd(G)$.
* page 3 : [iterated type partitions]({{< base >}}html/G1Cwmc) upper bounds [modular-width]({{< base >}}html/4bj71L) by a linear function -- By definition