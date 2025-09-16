# A partial $k$-arboretum of graphs with bounded treewidth by Bodlaender

[https://www.doi.org/10.1016/S0304-3975(97)00228-4](https://www.doi.org/10.1016/S0304-3975(97)00228-4)

```bibtex
@article{Bodlaender1998,
author = {Hans L. Bodlaender},
doi = {10.1016/S0304-3975(97)00228-4},
issn = {0304-3975},
journaltitle = {Theoretical Computer Science},
number = {1},
pages = {1--45},
title = {A partial $k$-arboretum of graphs with bounded treewidth},
volume = {209},
year = {1998},
}
```
* page 4 : [pathwidth]({{< base >}}html/VHClqR) upper bounds [treewidth]({{< base >}}html/5Q7fuR) by a linear function -- Lemma 3. (a) For all graphs $G$, $pathwidth(G) \ge treewidth(G)$. ...
* page 5 : [branch width]({{< base >}}html/lIcmuR) -- A \emph{branch decomposition} of a graph $G=(V,E)$ is a pair $(T=(I,F),\sigma)$, where $T$ is a tree with every node in $T$ of degree one of three, and $\sigma$ is a bijection from $E$ to the set of leaves in $T$. The \emph{order} of an edge $f \in F$ is the number of vertices $v \in V$, for which there exist adjacent edges $(v,w),(v,x) \in E$, such that the path in $T$ from $\sigma(v,w)$ to $\sigma(v,x)$ uses $f$. The \emph{width} of branch decomposition $(T=(I,F),\sigma)$, is the maximum order over all edges $f \in F$. The \emph{branchwidth} of $G$ is the minimum width over all branch decompositions of $G$.
* page 22 : [bandwidth]({{< base >}}html/aP5a38) -- Let $G=(V,E)$ be a graph, and let $f\colon V\to \{1,2,\dots,n\}$ be a linear ordering of $G$. 1. The \emph{bandwidth} of $f$ is $\max\{|f(v)-f(w)| \mid (v,w) \in E\}$. ... The bandwidth ... is the minimum bandwidth ... over all possible linear orderings of $G$.
* page 22 : [cutwidth]({{< base >}}html/TLx1pz) -- Let $G=(V,E)$ be a graph, and let $f\colon V\to \{1,2,\dots,n\}$ be a linear ordering of $G$. ... 2. The \emph{cutwidth} of $f$ is $\max_{1\le i\le n} |\{(u,v)\in E \mid f(u) \le i < f(v) \}|$. ... [cutwidth] of a graph $G$ is the minimum [cutwidth] ... over all possible linear orderings of $G$.
* page 22 : [topological bandwidth]({{< base >}}html/SnA7Eq) -- The \emph{topological bandwidth} of a graph $G$ is the minimum [bandwidth](../aP5a38) over all graphs $G'$ which are obtained by addition of an arbitrary number of vertices along edges of $G$.
* page 23 : [bandwidth]({{< base >}}html/aP5a38) upper bounds [pathwidth]({{< base >}}html/VHClqR) by a linear function -- Theorem 44. For every graph $G$, the pathwidth of $G$ is at most the bandwidth of $G$, ... Proof. Let $f \colon V\to \{1,\dots,n\}$ be a linear ordering of $G$ with bandwidth $k$. Then $(X_1,\dots,X_{n-k})$ with $X_i=\{f^{-1}(i), f^{-1}(i+1), \dots, f^{-1}(i+k)\}$ is a path decomposition of $G$ with pathwidth $k$. ...
* page 23 : [topological bandwidth]({{< base >}}html/SnA7Eq) upper bounds [pathwidth]({{< base >}}html/VHClqR) by a linear function -- Theorem 45. For every graph $G$, the pathwidth of $G$ is at most the topological band-width of $G$.
* page 24 : [cutwidth]({{< base >}}html/TLx1pz) upper bounds [pathwidth]({{< base >}}html/VHClqR) by a linear function -- Theorem 47. For every graph $G$, the pathwidth of $G$ is at most the cutwidth of $G$.
* page 24 : [pathwidth+maxdegree]({{< base >}}html/6BWcgd) upper bounds [cutwidth]({{< base >}}html/TLx1pz) by a linear function -- Theorem 49.
* page 24 : [cutwidth]({{< base >}}html/TLx1pz) upper bounds [pathwidth+maxdegree]({{< base >}}html/6BWcgd) by a linear function -- Theorem 49.
* page 34 : [outerplanar]({{< base >}}html/0oCyaG) upper bounds [treewidth]({{< base >}}html/5Q7fuR) by a constant -- Lemma 78. Every outerplanar graph $G=(V,E)$ has treewidth at most 2.
* page 37 : graph class [grid]({{< base >}}html/lfYXuK) is not constant [treewidth]({{< base >}}html/5Q7fuR) -- Lemma 88. The treewidth of an $n \times n$ grid graph ... is at least $n$.
* page 38 : [treewidth]({{< base >}}html/5Q7fuR) upper bounds [minimum degree]({{< base >}}html/GPmOeT) by a constant -- Lemma 90 (Scheffler [94]). Every graph of treewidth at most $k$ contains a vertex of degree at most $k$.