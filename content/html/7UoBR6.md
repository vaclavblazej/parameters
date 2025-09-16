# Twin-Cover: Beyond Vertex Cover in Parameterized Algorithmics by Ganian

[https://www.doi.org/10.1007/978-3-642-28050-4_21](https://www.doi.org/10.1007/978-3-642-28050-4_21)

```bibtex
@inproceedings{GanianTwinCover2012,
location = {Berlin, Heidelberg},
author = {Robert Ganian},
booktitle = {Parameterized and Exact Computation},
doi = {10.1007/978-3-642-28050-4_21},
isbn = {978-3-642-28050-4},
pages = {259--271},
publisher = {Springer},
series = {Lecture Notes in Computer Science},
title = {Twin-Cover: Beyond Vertex Cover in Parameterized Algorithmics},
year = {2012},
}
```
* page 262 : [twin-cover number]({{< base >}}html/MUnHA0) -- Definition 3.1. $X \subseteq V(G)$ is a twin-cover of $G$ if for every edge $e=\{a,b\} \in E(G)$ either 1. $a \in X$ or $b \in X$, or 2. $a$ and $b$ are twins, i.e. all other vertices are either adjacent to both $a$ and $b$ or none. We then say that $G$ has twin-cover number $k$ if $k$ is the minimum possible size of a twin-cover of $G$.
* page 262 : [twin-cover number]({{< base >}}html/MUnHA0) -- Definition 3.2. $X \subseteq V(G)$ is a twin-cover of $G$ if there exists a subgraph $G'$ of $G$ such that 1. $X \subseteq V(G')$ and $X$ is a vertex cover of $G'$. 2. $G$ can be obtained by iteratively adding twins to non-cover vertices in $G'$.
* page 263 : [complete]({{< base >}}html/EhdXNA) upper bounds [twin-cover number]({{< base >}}html/MUnHA0) by a constant -- We note that complete graphs indeed have a twin-cover of zero.
* page 263 : graph classes with bounded [twin-cover number]({{< base >}}html/MUnHA0) are not bounded [vertex cover]({{< base >}}html/4lp9Yj) -- The vertex cover of graphs of bounded twin-cover may be arbitrarily large.
* page 263 : graph classes with bounded [twin-cover number]({{< base >}}html/MUnHA0) are not bounded [treewidth]({{< base >}}html/5Q7fuR) -- There exists graphs with arbitrarily large twin-cover and bounded tree-width and vice-versa.
* page 263 : graph classes with bounded [treewidth]({{< base >}}html/5Q7fuR) are not bounded [twin-cover number]({{< base >}}html/MUnHA0) -- There exists graphs with arbitrarily large twin-cover and bounded tree-width and vice-versa.
* page 263 : [twin-cover number]({{< base >}}html/MUnHA0) upper bounds [clique-width]({{< base >}}html/wg5HuV) by a constant -- The clique-width of graphs of twin-cover $k$ is at most $k+2$.
* page 263 : [twin-cover number]({{< base >}}html/MUnHA0) upper bounds [rank-width]({{< base >}}html/fojquT) by a constant -- The rank-width and linaer rank-width of graph of twin-cover $k$ are at most $k+1$.
* page 263 : [twin-cover number]({{< base >}}html/MUnHA0) upper bounds [linear rank-width]({{< base >}}html/cHugsk) by a constant -- The rank-width and linaer rank-width of graph of twin-cover $k$ are at most $k+1$.