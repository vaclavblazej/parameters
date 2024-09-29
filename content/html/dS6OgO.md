# carving-width




<object data="../local_dS6OgO.pdf" type="application/pdf" width="100%" height="480px"><embed src="../local_dS6OgO.pdf"><p>This browser does not support PDFs. Please download the PDF to view it: <a href="../local_dS6OgO.pdf">Download PDF</a>.</p></embed></object>


<object data="../inclusions_dS6OgO.pdf" type="application/pdf" width="100%" height="480px"><embed src="../inclusions_dS6OgO.pdf"><p>This browser does not support PDFs. Please download the PDF to view it: <a href="../inclusions_dS6OgO.pdf">Download PDF</a>.</p></embed></object>

* 2013 [Belmonte2013]({{< base >}}html/sJ476m)
    * [carving-width]({{< base >}}html/dS6OgO) $k$ upper bounds [maximum degree]({{< base >}}html/UyQ5yM) by $\mathcal O(k)$ -- Observation 1. Let $G$ be a graph. Then $cw(G) \ge \Delta(G)$.
* 2010/08 [Sasak2010]({{< base >}}html/XlBXyo)
    * page 30 : [carving-width]({{< base >}}html/dS6OgO) $k$ upper bounds [maximum degree]({{< base >}}html/UyQ5yM) by $\mathcal O(k)$ -- Lemma 2.20 Carving-width of a graph $G$ is at least $\Delta(G)$ where $\Delta(G)$ is the maximum degree of a graph $G$.
    * page 30 : graph class [star]({{< base >}}html/CortlU) has unbounded [carving-width]({{< base >}}html/dS6OgO) -- Corollary 2.21 Carving-width of a star is $n-1$.
    * page 30 : [path]({{< base >}}html/ryPlqz) upper bounds [carving-width]({{< base >}}html/dS6OgO) by a constant -- ... path with carving-width 2.
    * page 38 : [cutwidth]({{< base >}}html/TLx1pz) $k$ upper bounds [carving-width]({{< base >}}html/dS6OgO) by $\mathcal O(k)$ -- Theorem 4.3 (carw $\prec$ cutw) Carving-width is bounded by cut-width.
    * page 49 : [carving-width]({{< base >}}html/dS6OgO) $k$ upper bounds [treewidth]({{< base >}}html/5Q7fuR) by $\mathcal O(k)$ -- Theorem 5.5 (tw $\prec$ carw) Tree-width is bounded by carving-width.
*  [https://en.wikipedia.org/wiki/Carving_width](https://en.wikipedia.org/wiki/Carving_width)
    * [carving-width]({{< base >}}html/dS6OgO) -- A carving can be described as an unrooted binary tree whose leaves are labeled with the vertices of the given graph. Removing any edge from this tree partitions the tree into two subtrees, and correspondingly partitions the vertices of the tree into two clusters. ... The width of a carving, defined in this way, is the maximum number of edges that connect two complementary clusters. The carving width of the graph is the minimum width of any hierarchical clustering.
*  [https://link.springer.com/article/10.1007/bf01215352](https://link.springer.com/article/10.1007/bf01215352)
    * [carving-width]({{< base >}}html/dS6OgO) -- Let $V$ be a finite set with $|V| \ge 2$. Two subsets $A,B\subseteq V$ \emph{cross} if $A\cap B$, $A-B$, $B-A$, $V-(A\cup B)$ are all non-empty. A \emph{carving} in $V$ is a set $\mathscr{C}$ of subsets of $V$ such that 1) $\emptyset, V \notin \mathscr{C}$ 2) no two members of $\mathscr{C}$ cross, and 3) $\mathscr{C}$ is maximal subject to (1) and (2). ... For $A \subseteq V(G)$, we denote by $\delta(A)$ ... the set of all edges with an end in $A$ and an end in $V(G)-A$. For each $e \in E(G)$, let $p(e) \ge 0$ be an integer. For $X \subseteq E(G)$ we denote $\sum_{e \in X}p(e)$ by $p(X)$, and if $|V(G)| \ge 2$ we define the \emph{$p$-carving-width} of $G$ to be the minimum, over all carvings $\mathscr{C}$ in $V(G)$, of the maximum, over all $A \in \mathscr{C}$, of $p(\delta(A))$. ... The \emph{carving-width} of $G$ is the $p$-carving-width of $G$ where $p(e)=1$ for every edge $e$.