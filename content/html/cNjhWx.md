# BuiXuan2011

[https://www.doi.org/10.1016/j.tcs.2011.05.022](https://www.doi.org/10.1016/j.tcs.2011.05.022)

```bibtex
@article{BuiXuan2011,
author = {Binh-Minh Bui-Xuan and Jan Arne Telle and Martin Vatshelle},
doi = {10.1016/j.tcs.2011.05.022},
issn = {0304-3975},
journaltitle = {Theoretical Computer Science},
number = {39},
pages = {5187--5204},
title = {Boolean-width of graphs},
volume = {412},
year = {2011},
}
```
* [boolean width]({{< base >}}html/A2jPWT) -- \textbf{Definition 1.} A decomposition tree of a graph $G$ is a pair $(T,\delta)$ where $T$ is a tree having internal nodes of degree three and $\delta$ a bijection between the leaf set of $T$ and the vertex set of $G$. Removing an edge from $T$ results in two subtrees, and in a cut $\{A,\comp{A}\}$ of $G$ given by the two subsets of $V(G)$ in bijection $\delta$ with the leaves of the two subtrees. Let $f\colon w^V \to \mathbb{R}$ be a symmetric function that is also called a cut function: $f(A)=f(\comp{A})$ for all $A\subseteq V(G)$. The $f$-width of $(T,\delta)$ is the maximum value of $f(A)$ over all cuts $\{A,\comp{A}\}$ of $G$ given by the removal of an edge of $T$. ... \textbf{Definition 2.} Let $G$ be a graph and $A \subseteq V(G)$. Define the set of unions of neighborhoods of $A$ across the cut $\{A,\comp{A}\}$ as $U(A) = \{Y \subseteq \comp{A} \mid \exists X \subseteq A \land Y=N(X)\cap \comp{A}\}. The \emph{bool-dim}$\colon 2^{V(G)} \to \mathbb{R}$ function of a graph $G$ is defined as $\mathrm{bool-dim}(A)=\log_2 |U(A)|$. Using Definition 1 with $f=\mathrm{bool-dim}$ we define the boolean-width of a decomposition tree, denoted by $boolw(T,\delta)$, and the boolean-width of a graph, denoted by $boolw(G)$.
* [boolean width]({{< base >}}html/A2jPWT) $k$ upper bounds [rank-width]({{< base >}}html/fojquT) by $2^{\mathcal O(k)}$ -- \textbf{Corollary 1.} For any graph $G$ and decomposition tree $(T,\gamma)$ of $G$ it holds that ... $\log_2 rw(G) \le boolw(G)$ ...
* [rank-width]({{< base >}}html/fojquT) $k$ upper bounds [boolean width]({{< base >}}html/A2jPWT) by $k^{\mathcal O(1)}$ -- \textbf{Corollary 1.} For any graph $G$ and decomposition tree $(T,\gamma)$ of $G$ it holds that ... $boolw(G) \le \frac 14 rw^2(G)+O(rw(G))$.