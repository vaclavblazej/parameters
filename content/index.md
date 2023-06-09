+++
+++
<!--this is a generated file-->

* Zoom with Ctrl+wheel and move with wheel & Shift+wheel
* Click nodes or circles at edges to jump to the relevant section with definition or inclusion proof.
* Any copied material has a source link -- this is the preferred way. Everything else will be slowly replaced.
* The sources are available [online](https://github.com/vaclavblazej/parameters), however, it is not trivial to work with.

<object data="parameters.pdf" type="application/pdf" width="100%" height="480px"><embed src="parameters.pdf"><p>This browser does not support PDFs. Please download the PDF to view it: <a href="main.pdf">Download PDF</a>.</p></embed></object>

# Parameters

## treewidth (TW) <span id=!IcKqSn></span>
* [source](https://en.wikipedia.org/wiki/Treewidth) ..., the treewidth of an undirected graph is an integer number which specifies, informally, how far the graph is from being a tree.
* [source](https://www.mimuw.edu.pl/~malcin/book/parameterized-algorithms.pdf) Very roughly, treewidth captures how similar a graph is to a tree. There are many ways to define ``tree-likeness'' of a graph; ... it appears that the approach most useful from algorithmic and graph theoretical perspectives, is to view tree-likeness of a graph $G$ as the existence of a structural decomposition of $G$ into pieces of bounded size that are connected in a tree-like fashion. This intuitive concept is formalized via the notions of a *tree decomposition* and the *treewidth* of a graph; the latter is a quantitative measure of how good a tree decomposition we can possibly obtain.
## pathwidth (PW) <span id=!nQhAoF></span>
* [source](https://mathworld.wolfram.com/Pathwidth.html) The pathwidth of a graph $G$, also called the interval thickness, vertex separation number, and node searching number, is one less than the size of the largest set in a path decomposition G.
## treedepth (TD) <span id=!KEP2qM></span>
* [source](https://en.wikipedia.org/wiki/Tree-depth) The tree-depth of a graph $G$ may be defined as the minimum height of a forest $F$ with the property that every edge of $G$ connects a pair of nodes that have an ancestor-descendant relationship to each other in $F$.
## feedback vertex set (FVS) <span id=!GNOiyB></span>
* [source](https://en.wikipedia.org/wiki/Feedback_vertex_set) ... a feedback vertex set (FVS) of a graph is a set of vertices whose removal leaves a graph without cycles... . The feedback vertex set number of a graph is the size of a smallest feedback vertex set.
* can be thought of as a *distance to forest*
## feedback edge set (FES) <span id=!HTk9PZ></span>
* [source](https://stackoverflow.com/questions/10791689/how-to-find-feedback-edge-set-in-undirected-graph) Let $G = (V,E)$ be an undirected graph. A set $F \subseteq E$ of edges is called a feedback-edge set if every cycle of $G$ has at least one edge in $F$.
## vertex cover (VC) <span id=!4lp9Yj></span>
* [source](https://en.wikipedia.org/wiki/Vertex_cover) ... set of vertices that includes at least one endpoint of every edge of the graph.
* can be thought of as a *distance to independent set*
## cliquewidth <span id=!U3jPaT></span>
* [source](https://en.wikipedia.org/wiki/Clique-width) ... the minimum number of labels needed to construct G by means of the following 4 operations: 1. Creation of a new vertex... 2. Disjoint union of two labeled graphs... 3. Joining by an edge every vertex labeled $i$ to every vertex labeled $j$, where $i \ne j$ 4. Renaming label $i$ to label $j$
## chromatic number <span id=!MB1Sr1></span>
* [source](https://mathworld.wolfram.com/ChromaticNumber.html) The chromatic number of a graph G is the smallest number of colors needed to color the vertices of G so that no two adjacent vertices share the same color (Skiena 1990, p. 210), ...
## degeneracy <span id=!m2q96O></span>
* [source](https://en.wikipedia.org/wiki/Degeneracy_(graph_theory)) ... the least $k$ for which there exists an ordering of the vertices of $G$ in which each vertex has fewer than $k$ neighbors that are earlier in the ordering.
## genus <span id=!gbaHdw></span>
* [source](https://en.wikipedia.org/wiki/Genus_(mathematics)#Graph_theory) The genus of a graph is the minimal integer $n$ such that the graph can be drawn without crossing itself on a sphere with $n$ handles.
## boxicity <span id=!j1rrOV></span>
* [source](https://en.wikipedia.org/wiki/Boxicity) The boxicity of a graph is the minimum dimension in which a given graph can be represented as an intersection graph of axis-parallel boxes.
## maximum degree <span id=!UyQ5yM></span>
* maximum degree of graph's vertices
## minimum degree <span id=!NCg08F></span>
* minimum degree of graph's vertices
## acyclic chromatic number <span id=!QoA8jA></span>
* [source](https://www.graphclasses.org/classes/par_31.html) The acyclic chromatic number of a graph $G$ is the smallest size of a vertex partition $V_1,\dots,V_\ell$ such that each $V_i$ is an independent set and for all $i,j$ that graph $G[V_i \cup V_j]$ does not contain a cycle.
* [source](https://en.wikipedia.org/wiki/Acyclic_coloring) ... an acyclic coloring is a (proper) vertex coloring in which every 2-chromatic subgraph is acyclic.
## h-index <span id=!gKbGUa></span>
* [source](https://link.springer.com/chapter/10.1007/978-3-642-03367-4_25) ... $h$ is the $h$-index of the graph, the maximum number such that the graph contains $h$ vertices of degree at least $h$.
## bandwidth <span id=!aP5a38></span>
* [source](https://en.wikipedia.org/wiki/Graph_bandwidth) (paraphrased) Label graph vertices with distinct integers. Bandwidth of this labelling is the maximum over label differences over all edges. Bandwidth of a graph is the minimum over all labellings.
## bisection bandwidth <span id=!wUdmUb></span>
* [source](https://en.wikipedia.org/wiki/Bisection_bandwidth) ... bisected into two equal-sized partitions, the bisection bandwidth of a network topology is the bandwidth available between the two partitions.
* [source](http://parallelcomp.github.io/Lecture3.pdf) [number of] links across smallest cut that divides nodes in two (nearly) equal parts
## maximum leaf number <span id=!BN92vX></span>
* [source](https://mathworld.wolfram.com/MaximumLeafNumber.html) ... the largest number of tree leaves in any of its spanning trees.
## distance to linear forest <span id=!9XDQCE></span>
* We can remove $k$ vertices to obtain a graph from the graph class mentioned in name of this parameter.
## distance to trees and disjoint cycles <span id=!599Nkv></span>
* We can remove $k$ vertices to obtain a graph from the graph class mentioned in name of this parameter.
## distance to cluster <span id=!TzspYl></span>
* We can remove $k$ vertices to obtain a graph from the graph class mentioned in name of this parameter.
## distance to interval <span id=!rr2exi></span>
* We can remove $k$ vertices to obtain a graph from the graph class mentioned in name of this parameter.
## distance to chordal <span id=!oi8KhK></span>
* We can remove $k$ vertices to obtain a graph from the graph class mentioned in name of this parameter.
## distance to outerplanar <span id=!ThJdP1></span>
* We can remove $k$ vertices to obtain a graph from the graph class mentioned in name of this parameter.
## distance to cograph <span id=!QiDXEo></span>
* We can remove $k$ vertices to obtain a graph from the graph class mentioned in name of this parameter.
## distance to constant components <span id=!bRBb5K></span>
* We can remove $k$ vertices to obtain a graph from the graph class mentioned in name of this parameter.
## vertex integrity <span id=!KVhJFB></span>
* Minimum $k$ such that there exists $k$ vertices whose removal results in connected components of sizes at most $k$.
## distance to stars <span id=!PwPrlq></span>
* We can remove $k$ vertices to obtain a graph from the graph class mentioned in name of this parameter.
## chordality <span id=!fTqo40></span>
* [source](https://onlinelibrary.wiley.com/doi/abs/10.1002/jgt.3190170210) The \emph{chordality} of a graph $G=(V,E)$ is defined as the minimum $k$ such that we can write $E=E_1,\cap\dots\cap E_k$ with each $(V,E_i)$ a chordal graph.
## distance to clique <span id=!7ugOaW></span>
* We can remove $k$ vertices to obtain a graph from the graph class mentioned in name of this parameter.
## clique cover number <span id=!VomShB></span>
* [source](https://en.wikipedia.org/wiki/Clique_cover) A minimum clique cover is a clique cover that uses as few cliques as possible. The minimum $k$ for which a clique cover exists is called the clique cover number of the given graph.
## maximum independent set <span id=!mHtXUU></span>
* [source](https://en.wikipedia.org/wiki/Maximal_independent_set) For a graph $G=(V,E)$, an independent set $S$ is a maximal independent set if for $v \in V$, one of the following is true: 1) $v \in S$ 2) $N(v) \cap S \ne \emptyset$ where $N(v)$ denotes the neighbors of $v$. ... the largest maximum independent set of a graph is called a maximum independent set.
## domination number <span id=!Gq0onN></span>
* [source](https://mathworld.wolfram.com/DominationNumber.html) The domination number $\gamma(G)$ of a graph $G$ is the minimum size of a dominating set of vertices in $G$ ...
## girth <span id=!AxyLAU></span>
* [source](https://en.wikipedia.org/wiki/Girth_(graph_theory)) In graph theory, the girth of an undirected graph is the length of a shortest cycle contained in the graph.
## distance to bipartite <span id=!T9s5sR></span>
* We can remove $k$ vertices to obtain a graph from the graph class mentioned in name of this parameter.
## distance to perfect <span id=!TLdoEo></span>
* We can remove $k$ vertices to obtain a graph from the graph class mentioned in name of this parameter.
## maximum clique <span id=!zYkYWx></span>
* [source](https://mathworld.wolfram.com/MaximumClique.html) A maximum clique of a graph $G$ is a clique (i.e., complete subgraph) of maximum possible size for $G$.
## average degree <span id=!X7CxTe></span>
* [source](https://bookdown.org/omarlizardo/_main/2-7-average-degree.html) Average degree is simply the average number of edges per node in the graph. ... Total Edges/Total Nodes=Average Degree
## domatic number <span id=!KRV6tI></span>
* [source](https://mathworld.wolfram.com/DomaticNumber.html) The maximum number of disjoint dominating sets in a domatic partition of a graph $G$ is called its domatic number $d(G)$. 
## vertex connectivity / distance to disconnected <span id=!CIEnCh></span>
* We can remove $k$ vertices to obtain a graph from the graph class mentioned in name of this parameter.
## twinwidth (tww) <span id=!VipBQc></span>
* [source](https://dl.acm.org/doi/10.1145/3486655) ... we consider a sequence of graph $G_n,G_{n-1},\dots,G_2,G_1$, where $G_n$ is the original graph $G$, $G_1$ is the one-vertex graph, $G_i$ has $i$ vertices, and $G_{i-1}$ is obtained from $G_i$ by performing a single contraction of two (non-necessarily adjacent) vertices. For every vertex $u \in V(G_i)$, let us denote by $u(G)$ the vertices of $G$ which have been contracted to $u$ along the sequence $G_n,\dots,G_i$. A pair of disjoint sets of vertices is homogeneous if, between these sets, there are either all possible edges or no edge at all. The red edges mentioned previously consist of all pairs $uv$ of vertices of $G_i$ such that $u(G)$ and $v(G)$ are not homogeneous in $G$. If the red degree of every $G_i$ is at most $d$, then $G_n,G_{n-1},\dots,G_2,G_1$ is called a sequence of $d$-contractions, or $d$-sequence. The twin-width of $G$ is the minimum $d$ for which there exists a sequence of $d$-contractions.
## book thickness <span id=!pKMM6O></span>
* [source](https://en.wikipedia.org/wiki/Book_embedding) ... a book embedding is a generalization of planar embedding of a graph to embeddings into a book, a collection of half-planes all having the same line as their boundary. Usually, the vertices of the graph are required to lie on this boundary line, called the spine, and the edges are required to stay within a single half-plane. The book thickness of a graph is the smallest possible number of half-planes for any book embedding of the graph.
## distance to planar <span id=!3Xj5rP></span>
* We can remove $k$ vertices to obtain a graph from the graph class mentioned in name of this parameter.
## diameter <span id=!QF9fW9></span>
* [source](https://en.wikipedia.org/wiki/Distance_(graph_theory)#Related_concepts) ... [diameter] is the greatest distance between any pair of vertices ...
## average distance <span id=!GPmPOT></span>
* [source](https://onlinelibrary.wiley.com/doi/abs/10.1002/jgt.3190120309) The average distance in a graph is defined as the average length of a shortest path between two vertices, taken over all pairs of vertices.
## maximum induced matching <span id=!wpeKEI></span>
* [source](https://www.sciencedirect.com/science/article/pii/0166218X9290275F?via%3Dihub) An induced matching in a graph G is a set of edges, no two of which meet a common node or are joined by an edge of G;
## maximum matching <span id=!veU7Jf></span>
* [source](https://www.graphclasses.org/classes/par_13.html) A matching in a graph is a subset of pairwise disjoint edges (any two edges that do not share an endpoint). The parameter maximum matching of a graph $G$ is the largest size of a matching in $G$.
## branch width <span id=!W0Iwpj></span>
* [source](https://en.wikipedia.org/wiki/Branch-decomposition) ... branch-decomposition of an undirected graph $G$ is a hierarchical clustering of the edges of $G$, represented by an unrooted binary tree $T$ with the edges of $G$ as its leaves. Removing any edge from $T$ partitions the edges of $G$ into two subgraphs, and the width of the decomposition is the maximum number of shared vertices of any pair of subgraphs formed in this way. The branchwidth of $G$ is the minimum width of any branch-decomposition of $G$.
## rank-width <span id=!IMmY3n></span>
* [source](https://www.sciencedirect.com/science/article/pii/S0095895605001528) see Section 6
## edge connectivity <span id=!W3n2Jv></span>
* [source](https://mathworld.wolfram.com/EdgeConnectivity.html) The edge connectivity, also called the line connectivity, of a graph is the minimum number of edges $\lambda(G)$ whose deletion from a graph $G$ disconnects $G$.
## neighborhood diversity <span id=!vMs3RS></span>
* [source](https://link.springer.com/article/10.1007/s00453-011-9554-x) We will say that two vertices $v, v'$ of a graph $G(V, E)$ have the same *type* iff they have the same colors and $N(v) \setminus \{v\} = N(v') \setminus \{v\}$, where $N(v)$ denotes the set of neighbors of $v$. ... A colored graph $G(V, E)$ has neighborhood diversity at most $w$, if there exists a partition of $V$ into at most $w$ sets, such that all the vertices in each set have the same type.
## shrub-depth <span id=!mOq1g7></span>
* [source](https://www.fi.muni.cz/~hlineny/papers/shrubdepth-warw18-slipp.pdf) Tree-model of $m$ colors and depth $d$: a rooted tree $T$ of height $d$, leaves are the vertices of $G$, each leaf has one of $m$ colors, an associated signature determining the edge set of $G$ as follows: for $i = 1,2,\dots,d$, let $u$ and $v$ be leaves with the least common ancestor at height $i$ in $T$, then $uv \in E(G)$ iff the color pair of $u,v$ is in the signature at height $i$.
## twin cover number <span id=!MUnHA0></span>
* Distance to cluster where all vertices of each clique are siblings.


# Relations

## [treewidth](#!IcKqSn) → [cliquewidth](#!U3jPaT) <span id=!9V7MFq></span>
* A nice tree decomposition yields a clique width decomposition of bounded number of labels as the forgotten vertices get one color and bag vertices get each its own color.
## [treewidth](#!IcKqSn) → [book thickness](#!pKMM6O) <span id=!2FIPpF></span>
## [pathwidth](#!nQhAoF) → [treewidth](#!IcKqSn) <span id=!c7lkhf></span>
* By definition. One parameter is special case of the other.
## [treedepth](#!KEP2qM) → [pathwidth](#!nQhAoF) <span id=!tKCHeJ></span>
* Saving the set of open vertices in a DFS over the tree treedepth after every step yields bags of a nice path decomposition.
## [treedepth](#!KEP2qM) → [diameter](#!QF9fW9) <span id=!6Kl5Pp></span>
* An unbounded diameter implies the class contains paths as subgraphs. Minimum treedepth to embed a path of length $n$ in a treedepth tree is $\log n$.
## [feedback vertex set](#!GNOiyB) → [distance to chordal](#!oi8KhK) <span id=!XqzgTC></span>
* By graph inclusion of the remaining graph classes.
## [feedback vertex set](#!GNOiyB) → [distance to bipartite](#!T9s5sR) <span id=!AbAK8n></span>
* By graph inclusion of the remaining graph classes.
## [feedback vertex set](#!GNOiyB) → [distance to outerplanar](#!ThJdP1) <span id=!slhzot></span>
* By graph inclusion of the remaining graph classes.
## [feedback vertex set](#!GNOiyB) → [distance to trees and disjoint cycles](#!599Nkv) <span id=!XuYoYh></span>
* By graph inclusion of the remaining graph classes.
## [feedback edge set](#!HTk9PZ) → [feedback vertex set](#!GNOiyB) <span id=!9Pdp4G></span>
* by a simple observation
## [feedback edge set](#!HTk9PZ) → [genus](#!gbaHdw) <span id=!12cxS9></span>
* Removing $k$ edges creates a forest that is embeddable into the plane. We now add one handle for each of the $k$ edges to get embedding into $k$-handle genus.
## [vertex cover](#!4lp9Yj) → [distance to stars](#!PwPrlq) <span id=!BWJDZs></span>
* By graph inclusion of the remaining graph classes.
## [vertex cover](#!4lp9Yj) → [distance to linear forest](#!9XDQCE) <span id=!VsrnoK></span>
* By graph inclusion of the remaining graph classes.
## [vertex cover](#!4lp9Yj) → [distance to constant components](#!bRBb5K) <span id=!yWSq1V></span>
* By graph inclusion of the remaining graph classes.
## [cliquewidth](#!U3jPaT) → [twinwidth](#!VipBQc) <span id=!5z03w7></span>
* Once two vertices have the same label they share their neighborhood with respect to all vertices they are connected to further. So to get a twinwidth sequence we merge all vertices that get same labels. Hence, red edges may occur only between different labels and the maximum red degree is bounded by the number of labels.
## [chromatic number](#!MB1Sr1) → [maximum clique](#!zYkYWx) <span id=!juphuT></span>
* by a simple observation
## [chromatic number](#!MB1Sr1) → [chordality](#!fTqo40) <span id=!DjfbnG></span>
## [degeneracy](#!m2q96O) → [chromatic number](#!MB1Sr1) <span id=!P4jZlH></span>
* Greedily color the vertices in order of the degeneracy ordering. As each vertex has at most $k$ colored predecesors we use at most $k+1$ colors.
## [degeneracy](#!m2q96O) → [average degree](#!X7CxTe) <span id=!ncjZd0></span>
* by a simple observation
## [genus](#!gbaHdw) → [book thickness](#!pKMM6O) <span id=!8JcAxM></span>
## [boxicity](#!j1rrOV) → [chordality](#!fTqo40) <span id=!ljoRXM></span>
## [maximum degree](#!UyQ5yM) → [h-index](#!gKbGUa) <span id=!PTu5gn></span>
* by a simple observation
## [minimum degree](#!NCg08F) → [edge connectivity](#!W3n2Jv) <span id=!9uKn16></span>
* by a simple observation
## [minimum degree](#!NCg08F) → [domatic number](#!KRV6tI) <span id=!l4bNpX></span>
* The vertex of minimum degree needs to be dominated in each of the sets. As the sets cannot overlap there can be at most $k+1$ of them.
## [acyclic chromatic number](#!QoA8jA) → [boxicity](#!j1rrOV) <span id=!JArOAD></span>
## [acyclic chromatic number](#!QoA8jA) → [degeneracy](#!m2q96O) <span id=!2WpXNT></span>
## [h-index](#!gKbGUa) → [acyclic chromatic number](#!QoA8jA) <span id=!pEPofm></span>
## [bandwidth](#!aP5a38) → [pathwidth](#!nQhAoF) <span id=!v6d2P7></span>
* Having bandwidth $k$, order vertices by their values. We create a bag for each vertex $u$ by taking $u$ and all vertices that have a value that is at most $k$ larger than the value of $u$. All edges fall into some bag and vertices span connected span of bags.
## [bandwidth](#!aP5a38) → [maximum degree](#!UyQ5yM) <span id=!e6NaBr></span>
* Each vertex has an integer $i$ and may be connected only to vertices whose difference from $i$ is at most $k$. There are at most $k$ bigger and $k$ smaller such neighbors.
## [bandwidth](#!aP5a38) → [bisection bandwidth](#!wUdmUb) <span id=!MKUFA8></span>
* Order vertices by their bandwidth integer. We split the graph in the middle of this ordering. There are at most roughly $k^2/2$ edges over this split.
## [bisection bandwidth](#!wUdmUb) → [edge connectivity](#!W3n2Jv) <span id=!sMfXRo></span>
* By definition. One parameter is special case of the other.
## [maximum leaf number](#!BN92vX) → [bandwidth](#!aP5a38) <span id=!mgFizL></span>
## [maximum leaf number](#!BN92vX) → [distance to linear forest](#!9XDQCE) <span id=!8oOsXL></span>
## [distance to linear forest](#!9XDQCE) → [feedback vertex set](#!GNOiyB) <span id=!lmKGuy></span>
* By graph inclusion of the remaining graph classes.
## [distance to linear forest](#!9XDQCE) → [distance to interval](#!rr2exi) <span id=!rHotfs></span>
* By graph inclusion of the remaining graph classes.
## [distance to linear forest](#!9XDQCE) → [pathwidth](#!nQhAoF) <span id=!KtFhkk></span>
* After removal of $k$ vertices the remaining class has a bounded width $w$. So by including the removed vertices in every bag, we can achieve decomposition of width $w+k$
## [distance to linear forest](#!9XDQCE) → [h-index](#!gKbGUa) <span id=!150N9P></span>
* After removal of $k$ vertices the remaining class has a bounded width $w$. So by including the removed vertices in every bag, we can achieve decomposition of width $w+k$
## [distance to trees and disjoint cycles](#!599Nkv) → [treewidth](#!IcKqSn) <span id=!B9l0ai></span>
* After removal of $k$ vertices the remaining class has a bounded width $w$. So by including the removed vertices in every bag, we can achieve decomposition of width $w+k$
## [distance to cluster](#!TzspYl) → [distance to interval](#!rr2exi) <span id=!FM1wVJ></span>
* By graph inclusion of the remaining graph classes.
## [distance to cluster](#!TzspYl) → [distance to cograph](#!QiDXEo) <span id=!7RXwqI></span>
* By definition. One parameter is special case of the other.
## [distance to interval](#!rr2exi) → [distance to chordal](#!oi8KhK) <span id=!fKpyMg></span>
* By graph inclusion of the remaining graph classes.
## [distance to interval](#!rr2exi) → [boxicity](#!j1rrOV) <span id=!hKjhJE></span>
* By definition. One parameter is special case of the other.
## [distance to chordal](#!oi8KhK) → [distance to perfect](#!TLdoEo) <span id=!piRTZw></span>
* By graph inclusion of the remaining graph classes.
## [distance to chordal](#!oi8KhK) → [chordality](#!fTqo40) <span id=!HqAvbm></span>
## [distance to outerplanar](#!ThJdP1) → [treewidth](#!IcKqSn) <span id=!voVCvr></span>
* After removal of $k$ vertices the remaining class has a bounded width $w$. So by including the removed vertices in every bag, we can achieve decomposition of width $w+k$
## [distance to outerplanar](#!ThJdP1) → [distance to planar](#!3Xj5rP) <span id=!ZiCzGe></span>
* By graph inclusion of the remaining graph classes.
## [distance to cograph](#!QiDXEo) → [distance to perfect](#!TLdoEo) <span id=!stwHRi></span>
* By graph inclusion of the remaining graph classes.
## [distance to cograph](#!QiDXEo) → [cliquewidth](#!U3jPaT) <span id=!crL8y9></span>
## [distance to cograph](#!QiDXEo) → [chordality](#!fTqo40) <span id=!i55YHW></span>
## [distance to cograph](#!QiDXEo) → [diameter](#!QF9fW9) <span id=!MgB6sE></span>
## [distance to constant components](#!bRBb5K) → [vertex integrity](#!KVhJFB) <span id=!wKsJTT></span>
* By graph inclusion of the remaining graph classes.
## [vertex integrity](#!KVhJFB) → [treedepth](#!KEP2qM) <span id=!10tIHQ></span>
* by a simple observation
## [distance to stars](#!PwPrlq) → [treedepth](#!KEP2qM) <span id=!g8LSVx></span>
* by a simple observation
## [distance to clique](#!7ugOaW) → [distance to cluster](#!TzspYl) <span id=!Tr2Ih9></span>
* By definition. One parameter is special case of the other.
## [distance to clique](#!7ugOaW) → [clique cover number](#!VomShB) <span id=!0mwDzZ></span>
* We cover the $k$ vertices of the modulator by cliques of size $1$ and cover the remaining clique by another one.
## [clique cover number](#!VomShB) → [maximum independent set](#!mHtXUU) <span id=!JtMcJB></span>
* Every clique of the clique cover partition may contain at most one vertex of the independent set.
## [maximum independent set](#!mHtXUU) → [domination number](#!Gq0onN) <span id=!Fxp100></span>
* Every maximal independent set is also a dominating set because any undominated vertex could be added to the independent set.
## [domination number](#!Gq0onN) → [diameter](#!QF9fW9) <span id=!UcXeli></span>
* An unbounded diameter implies a long path where no vertices that are more than $3$ apart may be dominated by the same dominating vertex, otherwise we could shorten the path. Hence, the number of dominating vertices is also unbounded.
## [distance to bipartite](#!T9s5sR) → [distance to perfect](#!TLdoEo) <span id=!ogyvLp></span>
* By graph inclusion of the remaining graph classes.
## [distance to bipartite](#!T9s5sR) → [chromatic number](#!MB1Sr1) <span id=!kXNdFI></span>
* Removed vertices get one color each and we need only $2$ colors for the rest.
## [average degree](#!X7CxTe) → [minimum degree](#!NCg08F) <span id=!YHgf7M></span>
* By definition. One parameter is special case of the other.
## [book thickness](#!pKMM6O) → [acyclic chromatic number](#!QoA8jA) <span id=!1LfCs5></span>
## [distance to planar](#!3Xj5rP) → [acyclic chromatic number](#!QoA8jA) <span id=!pEHP0K></span>
## [diameter](#!QF9fW9) → [average distance](#!GPmPOT) <span id=!hTp0QP></span>
* By definition. One parameter is special case of the other.
## [average distance](#!GPmPOT) → [girth](#!AxyLAU) <span id=!x9pao2></span>
## [maximum leaf number](#!BN92vX) → [feedback edge set](#!HTk9PZ) <span id=!v4djMN></span>
## [maximum induced matching](#!wpeKEI) → [diameter](#!QF9fW9) <span id=!gQqUuq></span>
## [maximum independent set](#!mHtXUU) → [maximum induced matching](#!wpeKEI) <span id=!uzK8uZ></span>
## [maximum matching](#!veU7Jf) → [maximum induced matching](#!wpeKEI) <span id=!ySKjme></span>
* By definition. One parameter is special case of the other.
## [branch width](#!W0Iwpj) → [treewidth](#!IcKqSn) <span id=!cYFhiJ></span>
## [treewidth](#!IcKqSn) → [branch width](#!W0Iwpj) <span id=!J94Xp2></span>
## [rank-width](#!IMmY3n) → [cliquewidth](#!U3jPaT) <span id=!paKd9Z></span>
* [source](https://www.sciencedirect.com/science/article/pii/S0095895605001528) Proposition 6.3
## [cliquewidth](#!U3jPaT) → [rank-width](#!IMmY3n) <span id=!zwiV6A></span>
* [source](https://www.sciencedirect.com/science/article/pii/S0095895605001528) Proposition 6.3
## [maximum matching](#!veU7Jf) → [vertex cover](#!4lp9Yj) <span id=!eg3i0f></span>
* [source](https://en.wikipedia.org/wiki/K%C5%91nig%27s_theorem_(graph_theory)) Kőnig's theorem
## [vertex cover](#!4lp9Yj) → [maximum matching](#!veU7Jf) <span id=!ZXIraS></span>
* [source](https://en.wikipedia.org/wiki/K%C5%91nig%27s_theorem_(graph_theory)) Kőnig's theorem
## [edge connectivity](#!W3n2Jv) → [vertex connectivity / distance to disconnected](#!CIEnCh) <span id=!haGgbI></span>
* by a simple observation
## [vertex cover](#!4lp9Yj) → [neighborhood diversity](#!vMs3RS) <span id=!tSmPSE></span>
* [source](https://link.springer.com/article/10.1007/s00453-011-9554-x) Construct $k$ singleton sets, one for each vertex in the vertex cover and at most $2^k$ additional sets, one for each subset of vertices of the vertex cover. ...
## [neighborhood diversity](#!vMs3RS) → [shrub-depth](#!mOq1g7) <span id=!WxT333></span>
## [twin cover number](#!MUnHA0) → [shrub-depth](#!mOq1g7) <span id=!1r3KyM></span>
## [twin cover number](#!MUnHA0) → [distance to cluster](#!TzspYl) <span id=!2f2OYD></span>
* By definition. One parameter is special case of the other.
## [vertex cover](#!4lp9Yj) → [twin cover number](#!MUnHA0) <span id=!7rSPl5></span>
* By graph inclusion of the remaining graph classes.
## [distance to clique](#!7ugOaW) → [neighborhood diversity](#!vMs3RS) <span id=!rJOrPy></span>
* [source](https://link.springer.com/article/10.1007/s00453-011-9554-x) Construct $k$ singleton sets, one for each vertex in the vertex cover and at most $2^k$ additional sets, one for each subset of vertices of the vertex cover. ...
## [treedepth](#!KEP2qM) → [shrub-depth](#!mOq1g7) <span id=!oWACte></span>
## [shrub-depth](#!mOq1g7) → [cliquewidth](#!U3jPaT) <span id=!knb7xY></span>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>The space above is here just to make the relative links work nicely even for the last entries :)