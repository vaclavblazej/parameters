# Tran2022

[https://fpt.akt.tu-berlin.de/publications/theses/BA-Duc-Long-Tran.pdf](https://fpt.akt.tu-berlin.de/publications/theses/BA-Duc-Long-Tran.pdf)

```bibtex
@thesis{Tran2022,
author = {Duc Long Tran},
month = {September},
institution = {Technische Universität Berlin},
title = {Expanding the Graph Parameter Hierarchy},
type = {Bachelor's Thesis},
url = {https://fpt.akt.tu-berlin.de/publications/theses/BA-Duc-Long-Tran.pdf},
year = {2022},
}
```
* page 15 : [twin-cover number]({{< base >}}html/MUnHA0) -- An edge $\{v,w\}$ is a twin edge if vertices $v$ and $w$ have the same neighborhood excluding each other. The twin cover number $tcn(G)$ of a graph $G$ is the size of a smallest set $V' \subseteq V(G)$ of vertices such that every edge in $E(G)$ is either a twin edge or incident to a vertex in $V'$
* page 15 : [edge clique cover number]({{< base >}}html/nYQDv6) -- The edge clique cover number $eccn(G)$ of a graph $G$ is the minimum number of complete subgraphs required such that each edge is contained in at least one of them.
* page 15 : [neighborhood diversity]({{< base >}}html/vMs3RS) -- The neighborhood diversity $nd(G)$ of a graph $G$ is the smallest number $k$ such that there is a $k$-partition $(V_1,\dots,V_k)$ of $G$, where each subset $V_i$, $i \in [k]$ is a module and is either a complete set or an independent set.
* page 15 : [modular-width]({{< base >}}html/4bj71L) -- The modular-width $mw(G)$ of a graph $G$ is the smallest number $h$ such that a $k$-partition $(V_1,\dots,V_k)$ of $G$ exists, where $k \le h$ and each subset $V_i$, $i \in [k]$ is a module and either contains a single vertex or for which the modular-subgraph $G[V_i]$ has a modular-width of $h$.
* page 17 : [boxicity]({{< base >}}html/a7MpiT) -- The boxicity of a graph $G$ is the minimum amount of interval graphs required, such that their intersecten results in $G$
* page 17 : [chordality]({{< base >}}html/fTqo40) -- The chordality of a graph $G$ is the minimum amount of chordal graphs required, such that their intersecten results in $G$
* page 19 : [vertex cover]({{< base >}}html/4lp9Yj) $k$ upper bounds [twin-cover number]({{< base >}}html/MUnHA0) by $\mathcal O(k)$ -- By definition
* page 19 : [complete]({{< base >}}html/EhdXNA) upper bounds [twin-cover number]({{< base >}}html/MUnHA0) by a constant -- Note that a clique of size $n$ has a twin cover number of $0$...
* page 19 : bounded [complete]({{< base >}}html/EhdXNA) does not imply bounded [vertex cover]({{< base >}}html/4lp9Yj) -- Note that a clique of size $n$ has ... a vertex cover number of $n-1$
* page 20 : bounded [twin-cover number]({{< base >}}html/MUnHA0) does not imply bounded [domatic number]({{< base >}}html/KRV6tI) -- Parameter is unbounded for the graph class of cliques.
* page 20 : bounded [twin-cover number]({{< base >}}html/MUnHA0) does not imply bounded [maximum clique]({{< base >}}html/q7zHeT) -- Parameter is unbounded for the graph class of cliques.
* page 20 : bounded [twin-cover number]({{< base >}}html/MUnHA0) does not imply bounded [edge connectivity]({{< base >}}html/JbqZoT) -- Parameter is unbounded for the graph class of cliques.
* page 23 : [edge clique cover number]({{< base >}}html/nYQDv6) $k$ upper bounds [neighborhood diversity]({{< base >}}html/vMs3RS) by $\mathcal O(k)$ -- Theorem 4.1. Edge Clique Cover Number strictly upper bounds Neighborhood Diversity.
* page 23 : bounded [neighborhood diversity]({{< base >}}html/vMs3RS) does not imply bounded [edge clique cover number]({{< base >}}html/nYQDv6) -- Theorem 4.1. Edge Clique Cover Number strictly upper bounds Neighborhood Diversity.
* page 24 : [distance to complete]({{< base >}}html/distance_to_EhdXNA) $k$ upper bounds [edge clique cover number]({{< base >}}html/nYQDv6) by $\mathcal O(k)$ -- Proposition 4.2. Disatnce to Clique strictly upper bounds Edge Clique Cover Number.
* page 24 : bounded [edge clique cover number]({{< base >}}html/nYQDv6) does not imply bounded [distance to complete]({{< base >}}html/distance_to_EhdXNA) -- Proposition 4.2. Disatnce to Clique strictly upper bounds Edge Clique Cover Number.
* page 25 : bounded [path]({{< base >}}html/ryPlqz) does not imply bounded [modular-width]({{< base >}}html/4bj71L) -- The Modular-width of a path $P$ with length $n > 3$ is $n$.
* page 26 : [modular-width]({{< base >}}html/4bj71L) $k$ upper bounds [clique width]({{< base >}}html/wg5HuV) by $\mathcal O(k)$ -- Proposition 4.6. Modular-width strictly upper bounds Clique-width.
* page 26 : bounded [clique width]({{< base >}}html/wg5HuV) does not imply bounded [modular-width]({{< base >}}html/4bj71L) -- Proposition 4.6. Modular-width strictly upper bounds Clique-width.