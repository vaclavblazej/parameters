# Twin-width I: Tractable `FO` Model Checking by Bonnet, Kim, Thomassé, Watrigant

[https://www.doi.org/10.1145/3486655](https://www.doi.org/10.1145/3486655)

```bibtex
@article{twinWidthI2021,
location = {New York, NY, USA},
articleno = {3},
author = {Édouard Bonnet and Eun Jung Kim and Stéphan Thomassé and Rémi Watrigant},
doi = {10.1145/3486655},
issn = {0004-5411},
journaltitle = {J. ACM},
month = {November},
number = {1},
publisher = {Association for Computing Machinery},
title = {Twin-width I: Tractable {FO} Model Checking},
volume = {69},
year = {2021},
}
```
* page 2 : [twin-width]({{< base >}}html/OrH7et) -- ... we consider a sequence of graphs $G_n,G_{n-1},\dots,G_2,G_1$, where $G_n$ is the original graph $G$, $G_1$ is the one-vertex graph, $G_i$ has $i$ vertices, and $G_{i-1}$ is obtained from $G_i$ by performing a single contraction of two (non-necessarily adjacent) vertices. For every vertex $u \in V(G_i)$, let us denote by $u(G)$ the vertices of $G$ which have been contracted to $u$ along the sequence $G_n,\dots,G_i$. A pair of disjoint sets of vertices is \emph{homogeneous} if, between these sets, there are either all possible edges or no edge at all. The red edges ... consist of all pairs $uv$ of vertices of $G_i$ such that $u(G)$ and $v(G)$ are not homogeneous in $G$. If the red degree of every $G_i$ is at most $d$, then $G_n,G_{n-1},\dots,G_2,G_1$ is called a \emph{sequence of $d$-contractions}, or \emph{$d$-sequence}. The twin-width of $G$ is the minimum $d$ for which there exists a sequence of $d$-contractions.
* page 14 : [boolean width]({{< base >}}html/A2jPWT) upper bounds [twin-width]({{< base >}}html/OrH7et) by an exponential function -- Theorem 3: Every graph with boolean-width $k$ has twin-width at most $2^{k+1}-1$.
* page 15 : [grid]({{< base >}}html/lfYXuK) upper bounds [twin-width]({{< base >}}html/OrH7et) by a constant -- Theorem 4.3. For every positive integers $d$ and $n$, the $d$-dimensional $n$-grid has twin-width at most $3d$.