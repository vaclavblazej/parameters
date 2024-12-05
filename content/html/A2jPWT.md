# boolean width




<object data="../local_A2jPWT.pdf" type="application/pdf" width="100%" height="480px"><embed src="../local_A2jPWT.pdf"><p>This browser does not support PDFs. Please download the PDF to view it: <a href="../local_A2jPWT.pdf">Download PDF</a>.</p></embed></object>


<object data="../inclusions_A2jPWT.pdf" type="application/pdf" width="100%" height="480px"><embed src="../inclusions_A2jPWT.pdf"><p>This browser does not support PDFs. Please download the PDF to view it: <a href="../inclusions_A2jPWT.pdf">Download PDF</a>.</p></embed></object>

*  [BuiXuan2011]({{< base >}}html/cNjhWx)
    * [boolean width]({{< base >}}html/A2jPWT) -- \textbf{Definition 1.} A decomposition tree of a graph $G$ is a pair $(T,\delta)$ where $T$ is a tree having internal nodes of degree three and $\delta$ a bijection between the leaf set of $T$ and the vertex set of $G$. Removing an edge from $T$ results in two subtrees, and in a cut $\{A,\comp{A}\}$ of $G$ given by the two subsets of $V(G)$ in bijection $\delta$ with the leaves of the two subtrees. Let $f\colon w^V \to \mathbb{R}$ be a symmetric function that is also called a cut function: $f(A)=f(\comp{A})$ for all $A\subseteq V(G)$. The $f$-width of $(T,\delta)$ is the maximum value of $f(A)$ over all cuts $\{A,\comp{A}\}$ of $G$ given by the removal of an edge of $T$. ... \textbf{Definition 2.} Let $G$ be a graph and $A \subseteq V(G)$. Define the set of unions of neighborhoods of $A$ across the cut $\{A,\comp{A}\}$ as $U(A) = \{Y \subseteq \comp{A} \mid \exists X \subseteq A \land Y=N(X)\cap \comp{A}\}. The \emph{bool-dim}$\colon 2^{V(G)} \to \mathbb{R}$ function of a graph $G$ is defined as $\mathrm{bool-dim}(A)=\log_2 |U(A)|$. Using Definition 1 with $f=\mathrm{bool-dim}$ we define the boolean-width of a decomposition tree, denoted by $boolw(T,\delta)$, and the boolean-width of a graph, denoted by $boolw(G)$.
    * [boolean width]({{< base >}}html/A2jPWT) upper bounds [rank-width]({{< base >}}html/fojquT) by an exponential function -- \textbf{Corollary 1.} For any graph $G$ and decomposition tree $(T,\gamma)$ of $G$ it holds that ... $\log_2 rw(G) \le boolw(G)$ ...
    * [rank-width]({{< base >}}html/fojquT) upper bounds [boolean width]({{< base >}}html/A2jPWT) by a polynomial function -- \textbf{Corollary 1.} For any graph $G$ and decomposition tree $(T,\gamma)$ of $G$ it holds that ... $boolw(G) \le \frac 14 rw^2(G)+O(rw(G))$.
*  [https://dl.acm.org/doi/10.1145/3486655](https://dl.acm.org/doi/10.1145/3486655)
    * [boolean width]({{< base >}}html/A2jPWT) upper bounds [twin-width]({{< base >}}html/reduced_UyQ5yM) by an exponential function -- Theorem 3: Every graph with boolean-width $k$ has twin-width at most $2^{k+1}-1$.
*  [Vatshelle2012]({{< base >}}html/nRO7AG)
    * page 42 : [boolean width]({{< base >}}html/A2jPWT) upper bounds [mim-width]({{< base >}}html/WmIFB1) by a linear function -- Theorem 4.2.10. Let $G$ be a graph, then $mimw(G) \le boolw(G) \le mimw(G) \log_2(n)$
*  [unknown source]({{< base >}}html/myit4D)
    * [clique-width]({{< base >}}html/wg5HuV) upper bounds [boolean width]({{< base >}}html/A2jPWT) by a linear function
    * [boolean width]({{< base >}}html/A2jPWT) upper bounds [clique-width]({{< base >}}html/wg5HuV) by an exponential function
    * [branch width]({{< base >}}html/lIcmuR) upper bounds [boolean width]({{< base >}}html/A2jPWT) by a linear function
    * [treewidth]({{< base >}}html/5Q7fuR) upper bounds [boolean width]({{< base >}}html/A2jPWT) by a computable function