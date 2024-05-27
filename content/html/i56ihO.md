# RobertsonSymour1986

[https://www.doi.org/10.1016/0196-6774(86)90023-4](https://www.doi.org/10.1016/0196-6774(86)90023-4)

```bibtex
@article{RobertsonSymour1986,
author = {Neil Robertson and Paul D. Seymour},
doi = {10.1016/0196-6774(86)90023-4},
issue = {3},
journaltitle = {Journal of Algorithms},
month = {September},
pages = {309--322},
title = {Graph minors. II. Algorithmic aspects of tree-width},
volume = {7},
year = {1986},
}
```
* page 1 : [treewidth]({{< base >}}html/5Q7fuR) -- A \emph{tree-decomposition} of $G$ is a family $(X_i \colon i\in I)$ of subsets of $V(G)$, together with a tree $T$ with $V(T)=I$, with the following properties. (W1) $\bigcup(X_i \colon i \in I)=V(G)$. (W2) Every edge of $G$ has both its ends in some $X_i$ ($i \in I$). (W3) For $i,j,k \in I$, if $j$ lies on the path of $T$ from $i$ to $k$ then $X_i \cap X_k \subseteq X_j$. The \emph{width} of the tree-decomposition is $\max(|X_i|-1 \colon i \in I)$. The tree-width of $G$ is the minimum $w \ge 0$ such that $G$ has a tree-decomposition of width $\le w$.
* page 1 : [treewidth]({{< base >}}html/5Q7fuR) -- Equivalently, the tree-width of $G$ is the minimum $w \ge 0$ such that $G$ is a subgraph of a ``chordal'' graph with all cliques of size at most $w + 1$.