# branch width




<object data="../local_lIcmuR.pdf" type="application/pdf" width="100%" height="480px"><embed src="../local_lIcmuR.pdf"><p>This browser does not support PDFs. Please download the PDF to view it: <a href="../local_lIcmuR.pdf">Download PDF</a>.</p></embed></object>


<object data="../inclusions_lIcmuR.pdf" type="application/pdf" width="100%" height="480px"><embed src="../inclusions_lIcmuR.pdf"><p>This browser does not support PDFs. Please download the PDF to view it: <a href="../inclusions_lIcmuR.pdf">Download PDF</a>.</p></embed></object>

* 1998 [Bodlaender1998]({{< base >}}html/BOFCWg)
    * page 5 : [branch width]({{< base >}}html/lIcmuR) -- A \emph{branch decomposition} of a graph $G=(V,E)$ is a pair $(T=(I,F),\sigma)$, where $T$ is a tree with every node in $T$ of degree one of three, and $\sigma$ is a bijection from $E$ to the set of leaves in $T$. The \emph{order} of an edge $f \in F$ is the number of vertices $v \in V$, for which there exist adjacent edges $(v,w),(v,x) \in E$, such that the path in $T$ from $\sigma(v,w)$ to $\sigma(v,x)$ uses $f$. The \emph{width} of branch decomposition $(T=(I,F),\sigma)$, is the maximum order over all edges $f \in F$. The \emph{branchwidth} of $G$ is the minimum width over all branch decompositions of $G$.
* 1991/07 [RobertsonSymour1991]({{< base >}}html/1hPzXs)
    * page 12 : [branch width]({{< base >}}html/lIcmuR) -- A \emph{branch-width} of a hypergraph $G$ is a pair $(T,\tau)$, where $T$ is a ternary tree and $\tau$ is a bijection from the set of leaves of $T$ to $E(G)$. The \emph{order} of an edge $e$ of $T$ is the number of vertices $v$ of $G$ such that there are leaves $t_1,t_2$ of $T$ in different components of $T \setminus e$, with $\tau(t_1),\tau(t_2)$ both incident with $v$. The \emph{width} of $(T,\tau)$ is the maximum order of the edges of $T$, and the \emph{branch-width} $\beta(G)$ of $G$ is the minimum width of all branch-decompositions of $G$ (or 0 if $|E(G)| \le 1$, when $G$ has no branch-decompositions).
    * page 16 : [treewidth]({{< base >}}html/5Q7fuR) $k$ upper bounds [branch width]({{< base >}}html/lIcmuR) by $\mathcal O(k)$ -- (5.1) For any hypergraph $G$, $\max(\beta(G), \gamma(G)) \le \omega(G) + 1 \le \max(\lfloor(3/2)\beta(G)\rfloor, \gamma(G), 1)$.
    * page 16 : [branch width]({{< base >}}html/lIcmuR) $k$ upper bounds [treewidth]({{< base >}}html/5Q7fuR) by $\mathcal O(k)$ -- (5.1) For any hypergraph $G$, $\max(\beta(G), \gamma(G)) \le \omega(G) + 1 \le \max(\lfloor(3/2)\beta(G)\rfloor, \gamma(G), 1)$.
*  [unknown]({{< base >}}html/myit4D)
    * [branch width]({{< base >}}html/lIcmuR) $k$ upper bounds [boolean width]({{< base >}}html/A2jPWT) by $\mathcal O(k)$
    * [branch width]({{< base >}}html/lIcmuR) $k$ upper bounds [rank-width]({{< base >}}html/fojquT) by $\mathcal O(k)$
*  [https://en.wikipedia.org/wiki/Branch-decomposition](https://en.wikipedia.org/wiki/Branch-decomposition)
    * [branch width]({{< base >}}html/lIcmuR) -- ... branch-decomposition of an undirected graph $G$ is a hierarchical clustering of the edges of $G$, represented by an unrooted binary tree $T$ with the edges of $G$ as its leaves. Removing any edge from $T$ partitions the edges of $G$ into two subgraphs, and the width of the decomposition is the maximum number of shared vertices of any pair of subgraphs formed in this way. The branchwidth of $G$ is the minimum width of any branch-decomposition of $G$.