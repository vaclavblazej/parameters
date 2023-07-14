import par_types
import par_processing

from par_types import Data

def export():
    return par_processing.postprocess(par_types.data)

################################################################################
## Sources and Common Citations ################################################
################################################################################

# Find these sources in main.bib

from par_types import Source, Cite

Torunczyk2023=Source("KpkMZB", "Torunczyk2023", [
    ])
Tran2022=Source("uXViPE", "Tran2022", [
    ])
SchroderThesis=Source("DYGiYb", "SchroderThesis", [
    Cite(id="3Ovt5i", source=Tran2022),
    ])
Diestel2017=Source("r2Lwky", "Diestel2017", [
    ])
Jansen2013=Source("FLOjic", "Jansen2013", [
    ])
BuiXuan2011=Source("cNjhWx", "BuiXuan2011", [
    ])
Oum2006=Source("1ZTWBd", "Oum2006", [
    ])
Corneil2005=Source("HCGunF", "Corneil2005", [
    ])

################################################################################
## Graph Classes ###############################################################
################################################################################

from par_types import GraphClass, Inclusion, ISGCI, Note, connected

#  r_partite=GraphClass("Klo2tD", "r-partite", [
    #  Cite(id="0MQIxu", source=Diestel2017, text="Let $r \\ge 2$ be an integer. A graph $G=(V, E)$ is called \\emph{$r$-partite} if $V$ admits a partition into $r$ classes such that every edge has its ends in diﬀerent classes: vertices in the same partition class must not be adjacent.", page=17),
    #  ])
bipartite=GraphClass("cLHJkW", "bipartite", [
    Cite(id="P1ExcE", source=Diestel2017, text="Instead of `2-partite' one usually says bipartite.", page=17),
    ISGCI(69),
    ])
block=GraphClass("QrxQsH", "block", [
    Note(id="2kG0kY", text="Every block (maximal 2-connected subgraph) is a clique."),
    ISGCI(93),
    ])
chordal=GraphClass("Cv1PaJ", "chordal", [
    Cite(id="wkrz7h", source=Diestel2017, text="... a graph is chordal (or triangulated) if each of its cycles of length at least $4$ has a chord, i.e. if it contains no induced cycles other than triangles.", page=135),
    ISGCI(32),
    ])
cluster=GraphClass("WAU7vf", "cluster", [
    Note(id="roSFzV", text="Disjoint union of complete graphs."),
    ISGCI(1237),
    ])
co_cluster=GraphClass("7HR4uV", "co-cluster", [
    Note(id="FDbIDy", text="Complete multipartite graph."),
    ISGCI(1248),
    ])
cograph=GraphClass("9Qd0Mx", "cograph", [
    ISGCI(151),
    ])
complete = connected("complete", cluster, [
    Cite(id="hxpfbI", source=Diestel2017, text="If all the vertices of $G$ are pairwise adjacent, then $G$ is \\emph{complete}.", page=3),
    ISGCI(1241),
    ])
const_components=GraphClass("FJ8gmU", "constant components", [
    Note(id="FvgORV", text="Disjoint union of components of constant size."),
    ])
forest=GraphClass("JngPPm", "forest", [
    Cite(id="8XlBpy", source=Diestel2017, text="An acyclic graph, one not containing any cycles, is called a \\emph{forest}.", page=13),
    ISGCI(342),
    ])
interval=GraphClass("p5skoj", "interval", [
    Cite(id="pMo8dB", source=Diestel2017, text="A graph $G$ is called an \\emph{interval graph} if there exists a set $\\{ I_v \\mid v \\in V(G) \\}$ of real intervals such that $I_u \\cap I_v \\ne \\emptyset$ if and only if $uv \\in E(G)$.", page=145),
    ISGCI(234),
    ])
isolated=GraphClass("LsiBbX", "isolated vertices", [
    Cite(id="T8RJcC", source=Diestel2017, text="A vertex of degree $0$ is \\emph{isolated}.", page=5),
    ISGCI(1247),
    ])
linear_forest=GraphClass("skQuFN", "linear forest", [
    Note(id="XK5Xxy", text="Disjoint union of paths."),
    ])
outerplanar=GraphClass("0oCyaG", "outerplanar", [
    Cite(id="6Q0kuL", source=Diestel2017, text="A graph is called outerplanar if it has a drawing in which every vertex lies on the boundary of the outer face.", page=115, note="The drawing needs to be planar."),
    ISGCI(110),
    ])
perfect=GraphClass("RmssrZ", "perfect", [
    Cite(id="54XChb", source=Diestel2017, text="A graph is called perfect if every induced subgraph $H \\subseteq G$ has chromatic number $\\chi(H)=\\omega(H)$, i.e. if the trivial lower bound of $\\omega(H)$ colours always suffices to colour the vertices of $H$.", page=135),
    ISGCI(56),
    ])
planar=GraphClass("loZ5LD", "planar", [
    Cite(id="eMZCoY", source=Diestel2017, text="When we draw a graph on a piece of paper, we naturally try to do this as transparently as possible. One obvious way to limit the mess created by all the lines is to avoid intersections. \\dots Graphs drawn in this way are called \\emph{plane graphs}; abstract graphs that can be drawn in this way are called \\emph{planar}.", page=89),
    ISGCI(43),
    ])
stars=GraphClass("10JR3F", "stars", [
    Note(id="51KDFn", text="Disjoint union of stars."),
    ISGCI(1297),
    ])
cycles=GraphClass("AGnF5Z", "disjoint cycles", [
    Note(id="cBDurK", text="All cycles in the graph are disjoint. Can contain arbitrary trees attached to and between the cycles.")
    ])
grid=GraphClass("lfYXuK", "grid", [
    Note(id="sp6LGE", text="Cartesian product of two paths."),
    ISGCI(464),
    ])

Inclusion(id="piRTZw", superclass=perfect, subclass=chordal, notes=[
    ])
Inclusion(id="stwHRi", superclass=perfect, subclass=cograph, notes=[
    ])
Inclusion(id="ogyvLp", superclass=perfect, subclass=bipartite, notes=[
    ])
Inclusion(id="FM1wVJ", superclass=interval, subclass=cluster, notes=[
    ])
Inclusion(id="rHotfs", superclass=interval, subclass=linear_forest, notes=[
    ])
Inclusion(id="fKpyMg", superclass=chordal, subclass=interval, notes=[
    ])
#  Inclusion(id="XqzgTC", superclass=chordal, subclass=forest, notes=[
    #  ])
#  Inclusion(id="KpN2Uj", superclass=cograph, subclass=cluster, notes=[
    #  ])
Inclusion(id="cZy5xs", superclass=cograph, subclass=co_cluster, notes=[
    ])
Inclusion(id="AbAK8n", superclass=bipartite, subclass=forest, notes=[
    ])
Inclusion(id="ZiCzGe", superclass=planar, subclass=outerplanar, notes=[
    ])
Inclusion(id="6TFVVG", superclass=co_cluster, subclass=complete, notes=[
    ])
Inclusion(id="2Jde0p", superclass=chordal, subclass=block, notes=[
    ])
Inclusion(id="DxYTTn", superclass=block, subclass=cluster, notes=[
    ])
Inclusion(id="slhzot", superclass=outerplanar, subclass=forest, notes=[
    ])
Inclusion(id="lmKGuy", superclass=forest, subclass=linear_forest, notes=[
    ])
Inclusion(id="hIuPAJ", superclass=planar, subclass=cycles, notes=[
    ])
Inclusion(id="eruyce", superclass=cycles, subclass=forest, notes=[
    ])
Inclusion(id="WJHhf0", superclass=block, subclass=forest, notes=[
    ])
Inclusion(id="VsrnoK", superclass=linear_forest, subclass=isolated, notes=[
    ])
Inclusion(id="E8B2Gj", superclass=forest, subclass=stars, notes=[
    ])
Inclusion(id="BWJDZs", superclass=stars, subclass=isolated, notes=[
    ])
Inclusion(id="yWSq1V", superclass=const_components, subclass=isolated, notes=[
    ])
Inclusion(id="HtdoRP", superclass=co_cluster, subclass=isolated, notes=[
    ])
Inclusion(id="1PLbSg", superclass=planar, subclass=grid, notes=[
    ])
Inclusion(id="RQcVkC", superclass=bipartite, subclass=grid, notes=[
    ])

################################################################################
## Topics connected to some parameters #########################################
################################################################################

from par_types import Topic

top_metric=Topic(id="wpYsel", name="metric", description="Typically used in metric spaces.")
top_drawing=Topic(id="lJJaYb", name="drawing", description="Closely tied to drawing the graph onto a topological space.")

################################################################################
## Parameters ##################################################################
################################################################################

from par_types import Parameter, AKA, distanceTo, Abbreviation

treewidth=Parameter(id="IcKqSn", name="treewidth", notes=[
    ISGCI(10),
    Cite(id="W4j934", url="https://en.wikipedia.org/wiki/Treewidth", text="..., the treewidth of an undirected graph is an integer number which specifies, informally, how far the graph is from being a tree."),
    Cite(id="xnhT1P", url="https://www.mimuw.edu.pl/~malcin/book/parameterized-algorithms.pdf", text="Very roughly, treewidth captures how similar a graph is to a tree. There are many ways to define ``tree-likeness'' of a graph; ... it appears that the approach most useful from algorithmic and graph theoretical perspectives, is to view tree-likeness of a graph $G$ as the existence of a structural decomposition of $G$ into pieces of bounded size that are connected in a tree-like fashion. This intuitive concept is formalized via the notions of a *tree decomposition* and the *treewidth* of a graph; the latter is a quantitative measure of how good a tree decomposition we can possibly obtain."),
    ])
pathwidth=Parameter(id="nQhAoF", name="pathwidth", notes=[
    ISGCI(9),
    Cite(id="dxaIhi", url="https://mathworld.wolfram.com/Pathwidth.html", text="The pathwidth of a graph $G$, also called the interval thickness, vertex separation number, and node searching number, is one less than the size of the largest set in a path decomposition G."),
    ])
treedepth=Parameter(id="KEP2qM", name="treedepth", notes=[
    ISGCI(18),
    Cite(id="QHJ1Kl", url="https://en.wikipedia.org/wiki/Tree-depth", text="The tree-depth of a graph $G$ may be defined as the minimum height of a forest $F$ with the property that every edge of $G$ connects a pair of nodes that have an ancestor-descendant relationship to each other in $F$."),
    ])
feedback_vertex_set=Parameter(id="GNOiyB", name="feedback vertex set", notes=[
    Cite(id="BJhqpe", url="https://en.wikipedia.org/wiki/Feedback_vertex_set", text="... a feedback vertex set (FVS) of a graph is a set of vertices whose removal leaves a graph without cycles... . The feedback vertex set number of a graph is the size of a smallest feedback vertex set."),
    Note(id="81zlqB", text="can be thought of as a *distance to forest*"),
    ])
feedback_edge_set=Parameter(id="HTk9PZ", name="feedback edge set", notes=[
    Cite(id="WP7pFA", url="https://stackoverflow.com/questions/10791689/how-to-find-feedback-edge-set-in-undirected-graph", text="Let $G=(V,E)$ be an undirected graph. A set $F \\subseteq E$ of edges is called a feedback-edge set if every cycle of $G$ has at least one edge in $F$."),
    ])
vertex_cover=Parameter(id="4lp9Yj", name="vertex cover", notes=[
    ISGCI(2),
    Cite(id="ez07Er", url="https://en.wikipedia.org/wiki/Vertex_cover", text="... set of vertices that includes at least one endpoint of every edge of the graph."),
    Note(id="DFiBbf", text="can be thought of as a *distance to independent set*"),
    ])
clique_width=Parameter(id="U3jPaT", name="clique-width", notes=[
    ISGCI(12),
    Cite(id="9Ckusi", url="https://en.wikipedia.org/wiki/Clique-width", text="... the minimum number of labels needed to construct G by means of the following 4 operations: 1. Creation of a new vertex... 2. Disjoint union of two labeled graphs... 3. Joining by an edge every vertex labeled $i$ to every vertex labeled $j$, where $i \\ne j$ 4. Renaming label $i$ to label $j$"),
    ])
linear_clique_width=Parameter(id="XQgWgv", name="linear clique-width", notes=[
    ])
chromatic_num=Parameter(id="MB1Sr1", name="chromatic number", notes=[
    ISGCI(19),
    Cite(id="VqwUmp", url="https://mathworld.wolfram.com/ChromaticNumber.html", text="The chromatic number of a graph G is the smallest number of colors needed to color the vertices of G so that no two adjacent vertices share the same color (Skiena 1990, p. 210), ..."),
    ])
degeneracy=Parameter(id="m2q96O", name="degeneracy", notes=[
    ISGCI(17),
    Cite(id="6LCwBu", url="https://en.wikipedia.org/wiki/Degeneracy_(graph_theory)", text="... the least $k$ for which there exists an ordering of the vertices of $G$ in which each vertex has fewer than $k$ neighbors that are earlier in the ordering."),
    ])
genus=Parameter(id="gbaHdw", name="genus", notes=[
    ISGCI(23),
    Cite(id="8ryhNq", url="https://en.wikipedia.org/wiki/Genus_(mathematics)#Graph_theory", text="The genus of a graph is the minimal integer $n$ such that the graph can be drawn without crossing itself on a sphere with $n$ handles."),
    top_drawing,
    ])
boxicity=Parameter(id="j1rrOV", name="boxicity", notes=[
    Cite(id="XWbXPm", url="https://en.wikipedia.org/wiki/Boxicity", text="The boxicity of a graph is the minimum dimension in which a given graph can be represented as an intersection graph of axis-parallel boxes."),
    Cite(id="eGC0vH", source=Tran2022, text="The boxicity of a graph $G$ is the minimum amount of interval graphs required, such that their intersecten results in $G$"),
    ])
max_degree=Parameter(id="UyQ5yM", name="maximum degree", notes=[
    ISGCI(28),
    Note(id="8tk4SI", text="maximum degree of graph's vertices"),
    ])
min_degree=Parameter(id="NCg08F", name="minimum degree", notes=[
    Note(id="CKNuj2", text="minimum degree of graph's vertices"),
    ])
acyclic_chromatic_number=Parameter(id="QoA8jA", name="acyclic chromatic number", notes=[
    ISGCI(31),
    Cite(id="cNSdgE", url="https://www.graphclasses.org/classes/par_31.html", text="The acyclic chromatic number of a graph $G$ is the smallest size of a vertex partition $V_1,\\dots,V_\\ell$ such that each $V_i$ is an independent set and for all $i,j$ that graph $G[V_i \\cup V_j]$ does not contain a cycle."),
    Cite(id="rj2m4h", url="https://en.wikipedia.org/wiki/Acyclic_coloring", text="... an acyclic coloring is a (proper) vertex coloring in which every 2-chromatic subgraph is acyclic."),
    ])
hindex=Parameter(id="gKbGUa", name="h-index", notes=[
    Cite(id="WY6oNX", url="https://link.springer.com/chapter/10.1007/978-3-642-03367-4_25", text="... $h$ is the $h$-index of the graph, the maximum number such that the graph contains $h$ vertices of degree at least $h$."),
    ])
bandwidth=Parameter(id="aP5a38", name="bandwidth", notes=[
    ISGCI(25),
    Cite(id="s7OvjQ", url="https://en.wikipedia.org/wiki/Graph_bandwidth", text="(paraphrased) Label graph vertices with distinct integers. Bandwidth of this labelling is the maximum over label differences over all edges. Bandwidth of a graph is the minimum over all labellings."),
    ])
topological_bandwidth=Parameter(id="SnA7Eq", name="topological bandwidth", notes=[
    Cite(id="PV6tGG", source=Jansen2013, text="The \\emph{topological bandwidth} of a graph $G$ is the minimum [bandwidth](#aP5a38) over all subdivisions of $G$"),
    ])
bisection_bandwidth=Parameter(id="wUdmUb", name="bisection bandwidth", notes=[
    Cite(id="iWUynL", url="https://en.wikipedia.org/wiki/Bisection_bandwidth", text="... bisected into two equal-sized partitions, the bisection bandwidth of a network topology is the bandwidth available between the two partitions."),
    Cite(id="AeRM2B", url="http://parallelcomp.github.io/Lecture3.pdf", text="(number of) links across smallest cut that divides nodes in two (nearly) equal parts"),
    ])
max_leaf_num=Parameter(id="BN92vX", name="maximum leaf number", notes=[
    ISGCI(22),
    Cite(id="Q3HJs5", url="https://mathworld.wolfram.com/MaximumLeafNumber.html", text="... the largest number of tree leaves in any of its spanning trees."),
    ])
distanceTo(linear_forest).notes += [
    ISGCI(24),
    ]
distanceTo(cluster).notes += [
    ISGCI(29),
    ]
distanceTo(outerplanar).notes += [
    ISGCI(26),
    ]
distanceTo(cograph).notes += [
    ISGCI(7),
    ]
vertex_integrity=Parameter(id="KVhJFB", name="vertex integrity", notes=[
    Note(id="aQQnbF", text="Minimum $k$ such that there exists $k$ vertices whose removal results in connected components of sizes at most $k$."),
    ])
chordality=Parameter(id="fTqo40", name="chordality", notes=[
    Cite(id="zYzUJ5", url="https://onlinelibrary.wiley.com/doi/abs/10.1002/jgt.3190170210", text="The \\emph{chordality} of a graph $G=(V,E)$ is defined as the minimum $k$ such that we can write $E=E_1,\\cap\\dots\\cap E_k$ with each $(V,E_i)$ a chordal graph."),
    Cite(id="gZtk6B", source=Tran2022, text="The chordality of a graph $G$ is the minimum amount of chordal graphs required, such that their intersecten results in $G$"),
    ])
distanceTo(complete).notes += [
    ISGCI(1),
    ]
clique_cover_num=Parameter(id="VomShB", name="clique cover number", notes=[
    Cite(id="jh0OIZ", url="https://en.wikipedia.org/wiki/Clique_cover", text="... is a partition of the vertices into cliques ... A minimum clique cover is a clique cover that uses as few cliques as possible. The minimum $k$ for which a clique cover exists is called the clique cover number of the given graph."),
    ])
max_independent_set=Parameter(id="mHtXUU", name="maximum independent set", notes=[
    ISGCI(8),
    Cite(id="0cYayY", url="https://en.wikipedia.org/wiki/Maximal_independent_set", text="For a graph $G=(V,E)$, an independent set $S$ is a maximal independent set if for $v \\in V$, one of the following is true: 1) $v \\in S$ 2), $N(v) \\cap S \\ne \\emptyset$ where $N(v)$ denotes the neighbors of $v$. ... the largest maximum independent set of a graph is called a maximum independent set."),
    ])
domination_num=Parameter(id="Gq0onN", name="domination number", notes=[
    ISGCI(5),
    Cite(id="82RsGb", url="https://mathworld.wolfram.com/DominationNumber.html", text="The domination number $\\gamma(G)$ of a graph $G$ is the minimum size of a dominating set of vertices in $G$ ..."),
    ])
girth=Parameter(id="AxyLAU", name="girth", notes=[
    Cite(id="u13WN1", url="https://en.wikipedia.org/wiki/Girth_(graph_theory)", text="In graph theory, the girth of an undirected graph is the length of a shortest cycle contained in the graph."),
    ])
odd_cycle_transversal=Parameter(id="gKMCdj", name="odd cycle transversal", notes=[
    ])
max_clique=Parameter(id="zYkYWx", name="maximum clique", notes=[
    ISGCI(27),
    Cite(id="PVi4lL", url="https://mathworld.wolfram.com/MaximumClique.html", text="A maximum clique of a graph $G$ is a clique (i.e., complete subgraph) of maximum possible size for $G$."),
    ])
average_degree=Parameter(id="X7CxTe", name="average degree", notes=[
    Cite(id="o6tFCJ", url="https://bookdown.org/omarlizardo/_main/2-7-average-degree.html", text="Average degree is simply the average number of edges per node in the graph. ... Total Edges/Total Nodes=Average Degree"),
    ])
domatic_num=Parameter(id="KRV6tI", name="domatic number", notes=[
    Cite(id="8eXjAy", url="https://mathworld.wolfram.com/DomaticNumber.html", text="The maximum number of disjoint dominating sets in a domatic partition of a graph $G$ is called its domatic number $d(G)$. "),
    ])
#  vertex_connectivity=Parameter(id="CIEnCh", name="vertex connectivity", notes=[
    #  Note(id="38YHVx", text="Minimum number of vertices $k$ such that the graph becomes disconnected."),
    #  AKA("distance to disconnected"),
    #  ])
twin_width=Parameter(id="VipBQc", name="twin-width", notes=[
    Cite(id="nyaOye", url="https://dl.acm.org/doi/10.1145/3486655", text="... we consider a sequence of graph $G_n,G_{n-1},\\dots,G_2,G_1$, where $G_n$ is the original graph $G$, $G_1$ is the one-vertex graph, $G_i$ has $i$ vertices, and $G_{i-1}$ is obtained from $G_i$ by performing a single contraction of two (non-necessarily adjacent) vertices. For every vertex $u \\in V(G_i)$, let us denote by $u(G)$ the vertices of $G$ which have been contracted to $u$ along the sequence $G_n,\\dots,G_i$. A pair of disjoint sets of vertices is homogeneous if, between these sets, there are either all possible edges or no edge at all. The red edges mentioned previously consist of all pairs $uv$ of vertices of $G_i$ such that $u(G)$ and $v(G)$ are not homogeneous in $G$. If the red degree of every $G_i$ is at most $d$, then $G_n,G_{n-1},\\dots,G_2,G_1$ is called a sequence of $d$-contractions, or $d$-sequence. The twin-width of $G$ is the minimum $d$ for which there exists a sequence of $d$-contractions."),
    ])
book_thickness=Parameter(id="pKMM6O", name="book thickness", notes=[
    ISGCI(32),
    Cite(id="YGmwCG", url="https://en.wikipedia.org/wiki/Book_embedding", text="... a book embedding is a generalization of planar embedding of a graph to embeddings into a book, a collection of half-planes all having the same line as their boundary. Usually, the vertices of the graph are required to lie on this boundary line, called the spine, and the edges are required to stay within a single half-plane. The book thickness of a graph is the smallest possible number of half-planes for any book embedding of the graph."),
    top_drawing,
    ])
distanceTo(planar).notes += [
    top_drawing,
    ]
diameter=Parameter(id="QF9fW9", name="diameter", notes=[
    ISGCI(6),
    Cite(id="055mG5", url="https://en.wikipedia.org/wiki/Distance_(graph_theory)#Related_concepts", text="... [diameter] is the greatest distance between any pair of vertices ..."),
    ])
average_distance=Parameter(id="GPmPOT", name="average distance", notes=[
    Cite(id="GfSsR4", url="https://onlinelibrary.wiley.com/doi/abs/10.1002/jgt.3190120309", text="The average distance in a graph is defined as the average length of a shortest path between two vertices, taken over all pairs of vertices."),
    ])
max_induced_matching=Parameter(id="wpeKEI", name="maximum induced matching", notes=[
    ISGCI(14),
    Cite(id="TKnuNP", url="https://www.sciencedirect.com/science/article/pii/0166218X9290275F?via%3Dihub", text="An induced matching in a graph G is a set of edges, no two of which meet a common node or are joined by an edge of G;"),
    ])
max_matching=Parameter(id="veU7Jf", name="maximum matching", notes=[
    ISGCI(13),
    Cite(id="f3q99d", url="https://www.graphclasses.org/classes/par_13.html", text="A matching in a graph is a subset of pairwise disjoint edges (any two edges that do not share an endpoint). The parameter maximum matching of a graph $G$ is the largest size of a matching in $G$."),
    ])
branch_width=Parameter(id="W0Iwpj", name="branch width", notes=[
    ISGCI(11),
    Cite(id="ZhBkjd", url="https://en.wikipedia.org/wiki/Branch-decomposition", text="... branch-decomposition of an undirected graph $G$ is a hierarchical clustering of the edges of $G$, represented by an unrooted binary tree $T$ with the edges of $G$ as its leaves. Removing any edge from $T$ partitions the edges of $G$ into two subgraphs, and the width of the decomposition is the maximum number of shared vertices of any pair of subgraphs formed in this way. The branchwidth of $G$ is the minimum width of any branch-decomposition of $G$."),
    ])
rank_width=Parameter(id="IMmY3n", name="rank-width", notes=[
    ISGCI(20),
    Cite(id="pjVGlR", url="https://www.sciencedirect.com/science/article/pii/S0095895605001528", text="see Section 6"),
    ])
edge_connectivity=Parameter(id="W3n2Jv", name="edge connectivity", notes=[
    Cite(id="ZunX1e", url="https://mathworld.wolfram.com/EdgeConnectivity.html", text="The edge connectivity, also called the line connectivity, of a graph is the minimum number of edges $\\lambda(G)$ whose deletion from a graph $G$ disconnects $G$."),
    ])
neighborhood_diversity=Parameter(id="vMs3RS", name="neighborhood diversity", notes=[
    Cite(id="L2KX25", url="https://link.springer.com/article/10.1007/s00453-011-9554-x", text="We will say that two vertices $v, v'$ of a graph $G(V, E)$ have the same *type* iff they have the same colors and $N(v) \\setminus \\{v\\}=N(v') \\setminus \\{v\\}$, where $N(v)$ denotes the set of neighbors of $v$. ... A colored graph $G(V, E)$ has neighborhood diversity at most $w$, if there exists a partition of $V$ into at most $w$ sets, such that all the vertices in each set have the same type."),
    Cite(id="iAkCJ3", source=Tran2022, text="The neighborhood diversity $nd(G)$ of a graph $G$ is the smallest number $k$ such that there is a $k$-partition $(V_1,\\dots,V_k)$ of $G$, where each subset $V_i$, $i \\in [k]$ is a module and is either a complete set or an independent set."),
    ])
shrub_depth=Parameter(id="mOq1g7", name="shrub-depth", notes=[
    Cite(id="4Dua5N", url="https://www.fi.muni.cz/~hlineny/papers/shrubdepth-warw18-slipp.pdf", text="Tree-model of $m$ colors and depth $d$: a rooted tree $T$ of height $d$, leaves are the vertices of $G$, each leaf has one of $m$ colors, an associated signature determining the edge set of $G$ as follows: for $i=1,2,\\dots,d$, let $u$ and $v$ be leaves with the least common ancestor at height $i$ in $T$, then $uv \\in E(G)$ iff the color pair of $u,v$ is in the signature at height $i$."),
    ])
twin_cover_num=Parameter(id="MUnHA0", name="twin cover number", notes=[
    Note(id="nTIDMU", text="Distance to cluster where all vertices of each clique are siblings."),
    Cite(id="J1sHj8", source=Tran2022, text="An edge $\\{v,w\\}$ is a twin edge if vertices $v$ and $w$ have the same neighborhood excluding each other. The twin cover number $tcn(G)$ of a graph $G$ is the size of a smallest set $V' \\subseteq V(G)$ of vertices such that every edge in $E(G)$ is either a twin edge or incident to a vertex in $V'$"),
    ])
inf_flip_width=Parameter(id="gNhjIg", name="inf-flip-width", notes=[
    Abbreviation("fw"),
    Cite(id="9VHraO", source=Torunczyk2023, text="See radius-r flip-width for $r=\\infty$."),
    ])
r_flip_width=Parameter(id="nMKJBg", name="radius-r flip-width", notes=[
    Abbreviation("fwr"),
    Cite(id="gxeVOT", source=Torunczyk2023, text="The radius-$r$ flip-width of a graph $G$, denoted $fwr (G)$, is the smallest number $k \\in \\mathbb{N}$ such that the cops have a winning strategy in the flipper game of radius $r$ and width $k$ on $G$"),
    ])
boolean_width=Parameter(id="XPNgY0", name="boolean-width", notes=[
    ISGCI(21),
    Cite(id="L7aY6D", source=BuiXuan2011, text="\\textbf{Definition 1.} A decomposition tree of a graph $G$ is a pair $(T,\\delta)$ where $T$ is a tree having internal nodes of degree three and $\\delta$ a bijection between the leaf set of $T$ and the vertex set of $G$. Removing an edge from $T$ results in two subtrees, and in a cut $\\{A,\\comp{A}\\}$ of $G$ given by the two subsets of $V(G)$ in bijection $\\delta$ with the leaves of the two subtrees. Let $f\\colon w^V \\to \\mathbb{R}$ be a symmetric function that is also called a cut function: $f(A)=f(\\comp{A})$ for all $A\\subseteq V(G)$. The $f$-width of $(T,\\delta)$ is the maximum value of $f(A)$ over all cuts $\\{A,\\comp{A}\\}$ of $G$ given by the removal of an edge of $T$. ... \\textbf{Definition 2.} Let $G$ be a graph and $A \\subseteq V(G)$. Define the set of unions of neighborhoods of $A$ across the cut $\\{A,\\comp{A}\\}$ as $U(A) = \\{Y \\subseteq \\comp{A} \\mid \\exists X \\subseteq A \\land Y=N(X)\\cap \\comp{A}\\}. The \\emph{bool-dim}$\\colon 2^{V(G)} \\to \\mathbb{R}$ function of a graph $G$ is defined as $\\mathrm{bool-dim}(A)=\\log_2 |U(A)|$. Using Definition 1 with $f=\\mathrm{bool-dim}$ we define the boolean-width of a decomposition tree, denoted by $boolw(T,\\delta)$, and the boolean-width of a graph, denoted by $boolw(G)$."),
    ])
carvingwidth=Parameter(id="dS6OgO", name="carvingwidth", notes=[
    ISGCI(16),
    Cite(id="bnOBjM", url="https://link.springer.com/article/10.1007/bf01215352", text="Let $V$ be a finite set with $|V| \\ge 2$. Two subsets $A,B\\subseteq V$ \\emph{cross} if $A\\cap B$, $A-B$, $B-A$, $V-(A\\cup B)$ are all non-empty. A \\emph{carving} in $V$ is a set $\\mathscr{C}$ of subsets of $V$ such that \\begin{enumerate} \\item $\\emptyset, V \\notin \\mathscr{C}$ \\item no two members of $\\mathscr{C}$ cross, and \\item $\\mathscr{C}$ is maximal subject to (1) and (2). ... For $A \\subseteq V(G)$, we denote by $\\delta(A)$ ... the set of all edges with an end in $A$ and an end in $V(G)-A$. For each $e \\in E(G)$, let $p(e) \\ge 0$ be an integer. For $X \\subseteq E(G)$ we denote $\\sum_{e \\in X}p(e)$ by $p(X)$, and if $|V(G)| \\ge 2$ we define the \\emph{$p$-carving-width} of $G$ to be the minimum, over all carvings $\\mathscr{C}$ in $V(G)$, of the maximum, over all $A \\in \\mathscr{C}$, of $p(\\delta(A))$. ... The \\emph{carving-width} of $G$ is the $p$-carving-width of $G$ where $p(e)=1$ for every edge $e$."),
    ])
cutwidth=Parameter(id="TLx1pz", name="cutwidth", notes=[
    ISGCI(15),
    ])
distanceTo(block).notes += [
    ISGCI(30),
    ]
distanceTo(co_cluster).notes += [
    ISGCI(3),
    ]
edge_clique_cover=Parameter(id="nYQDv6", name="edge clique cover number", notes=[
    Cite(id="MlTT7n", source=Tran2022, text="The edge clique cover number $eccn(G)$ of a graph $G$ is the minimum number of complete subgraphs required such that each edge is contained in at least one of them."),
    ])
modular_width=Parameter(id="4bj71L", name="modular-width", notes=[
    Cite(id="i3su9L", source=Tran2022, text="The modular-width $mw(G)$ of a graph $G$ is the smallest number $h$ such that a $k$-partition $(V_1,\\dots,V_k)$ of $G$ exists, where $k \\le h$ and each subset $V_i$, $i \\in [k]$ is a module and either contains a single vertex or for which the modular-subgraph $G[V_i]$ has a modular-width of $h$."),
    ])
c_closure=Parameter(id="ou9VU1", name="c-closure", notes=[
    ])

################################################################################
## Parameter Relations #########################################################
################################################################################

from par_types import UpperBound, HasBounded, HasUnbounded, Equivalent
from par_types import LINEAR, POLYNOMIAL, EXPONENTIAL


definition=Note(id="DQzjIV", text="By definition. One parameter is special case of the other.", upper_bound=LINEAR)
simple=Note(id="aQyAEM", text="by a simple observation")


UpperBound(id="9V7MFq", fr=treewidth, to=clique_width, notes=[
    #  Note(id="DKZYEb", text="A nice tree decomposition yields a clique width decomposition of bounded number of labels as the forgotten vertices get one color and bag vertices get each its own color.", upper_bound=LINEAR),
    Cite(id="sGBrPC", source=Corneil2005, text="\\dots the clique-width of $G$ is at most $3 * 2k - 1$ and, more importantly, that there is an exponential lower bound on this relationship. In particular, for any $k$, there is a graph $G$ with treewidth equal to $k$, where the clique-width of $G$ is at least $2\\lfloor k/2\\rfloor-1$.", upper_bound=EXPONENTIAL),
    ])
UpperBound(id="c7lkhf", fr=pathwidth, to=treewidth, notes=[
    definition
    ])
UpperBound(id="tKCHeJ", fr=treedepth, to=pathwidth, notes=[
    Note(id="q3qJkr", text="Saving the set of open vertices in a DFS over the tree treedepth after every step yields bags of a nice path decomposition.", upper_bound=LINEAR),
    ])
UpperBound(id="6Kl5Pp", fr=treedepth, to=diameter, notes=[
    Note(id="7tFsi6", text="An unbounded diameter implies the class contains paths as subgraphs. Minimum treedepth to embed a path of length $n$ in a treedepth tree is $\\log n$."),
    Cite(id="R9eI61", source=SchroderThesis, text="Proposition 3.1", upper_bound=LINEAR),
    ])
UpperBound(id="9Pdp4G", fr=feedback_edge_set, to=feedback_vertex_set, notes=[
    Note(id="5sq1SD", text="Given solution to feedback edge set one can remove one vertex incident to the solution edges to obtain feedback vertex set.", upper_bound=LINEAR),
    ])
UpperBound(id="12cxS9", fr=feedback_edge_set, to=genus, notes=[
    Note(id="8dQ8Us", text="Removing $k$ edges creates a forest that is embeddable into the plane. We now add one handle for each of the $k$ edges to get embedding into $k$-handle genus.", upper_bound=LINEAR),
    ])
UpperBound(id="5z03w7", fr=boolean_width, to=twin_width, notes=[
    Cite(id="08lETp", url="https://dl.acm.org/doi/10.1145/3486655", text="Theorem 3: Every graph with boolean-width $k$ has twin-width at most $2^{k+1}-1$.", upper_bound=EXPONENTIAL),
    ])
UpperBound(id="juphuT", fr=chromatic_num, to=max_clique, notes=[
    Note(id="K0Bc61", text="Unbounded clique implies the number of needed colors is unbounded.", upper_bound=LINEAR),
    ])
UpperBound(id="P4jZlH", fr=degeneracy, to=chromatic_num, notes=[
    Note(id="uKFrrb", text="Greedily color the vertices in order of the degeneracy ordering. As each vertex has at most $k$ colored predecesors we use at most $k+1$ colors.", upper_bound=LINEAR),
    ])
UpperBound(id="ncjZd0", fr=degeneracy, to=average_degree, notes=[
    Note(id="gLjejq", text="Removing a vertex of degree $d$ increases the value added to the sum of all degrees by at most $2d$, hence, the average is no more than twice the degeneracy.", upper_bound=LINEAR),
    ])
UpperBound(id="PTu5gn", fr=max_degree, to=hindex, notes=[
    Note(id="q5QDXg", text="As h-index seeks $k$ vertices of degree $k$ it is trivially upper bound by maximum degree.", upper_bound=LINEAR),
    ])
UpperBound(id="9uKn16", fr=min_degree, to=edge_connectivity, notes=[
    Note(id="1MAoyr", text="Removing edges incident to the minimum degree vertex disconnects the graph.", upper_bound=LINEAR),
    ])
UpperBound(id="l4bNpX", fr=min_degree, to=domatic_num, notes=[
    Note(id="UYpwYn", text="The vertex of minimum degree needs to be dominated in each of the sets. As the sets cannot overlap there can be at most $k+1$ of them.", upper_bound=LINEAR),
    ])
UpperBound(id="v6d2P7", fr=bandwidth, to=pathwidth, notes=[
    Note(id="kiza4J", text="Having bandwidth $k$, order vertices by their values. We create a bag for each vertex $u$ by taking $u$ and all vertices that have a value that is at most $k$ larger than the value of $u$. All edges fall into some bag and vertices span connected span of bags.", upper_bound=LINEAR),
    ])
UpperBound(id="e6NaBr", fr=bandwidth, to=max_degree, notes=[
    Note(id="waxvtz", text="Each vertex has an integer $i$ and may be connected only to vertices whose difference from $i$ is at most $k$. There are at most $k$ bigger and $k$ smaller such neighbors.", upper_bound=LINEAR),
    ])
UpperBound(id="MKUFA8", fr=bandwidth, to=bisection_bandwidth, notes=[
    Note(id="LyJWeW", text="Order vertices by their bandwidth integer. We split the graph in the middle of this ordering. There are at most roughly $k^2/2$ edges over this split.", upper_bound=POLYNOMIAL),
    ])
UpperBound(id="sMfXRo", fr=bisection_bandwidth, to=edge_connectivity, notes=[
    definition
    ])
UpperBound(id="KtFhkk", fr=distanceTo(linear_forest), to=pathwidth, notes=[
    Note(id="d2ZJIh", text="After removal of $k$ vertices the remaining class has a bounded width $w$. So by including the removed vertices in every bag, we can achieve decomposition of width $w+k$", upper_bound=LINEAR),
    ])
UpperBound(id="150N9P", fr=distanceTo(linear_forest), to=hindex, notes=[
    Cite(id="dohKmq", source=SchroderThesis, text="Proposition 3.2", upper_bound=LINEAR),
    ])
UpperBound(id="B9l0ai", fr=distanceTo(cycles), to=treewidth, notes=[
    Note(id="d2ZJIh", text="After removal of $k$ vertices the remaining class has a bounded width $w$. So by including the removed vertices in every bag, we can achieve decomposition of width $w+k$", upper_bound=LINEAR),
    ])
UpperBound(id="hKjhJE", fr=distanceTo(interval), to=boxicity, notes=[
    definition
    ])
UpperBound(id="voVCvr", fr=distanceTo(outerplanar), to=treewidth, notes=[
    Note(id="d2ZJIh", text="After removal of $k$ vertices the remaining class has a bounded width $w$. So by including the removed vertices in every bag, we can achieve decomposition of width $w+k$", upper_bound=LINEAR),
    ])
UpperBound(id="10tIHQ", fr=vertex_integrity, to=treedepth, notes=[
    Note(id="VS44M7", text="First, treedepth removes vertices of the modulator, then it iterates through remaining components one by one.", upper_bound=LINEAR),
    ])
UpperBound(id="wKsJTT", fr=distanceTo(const_components), to=vertex_integrity, notes=[
    Note(id="D0wE7A", text="The remaining components in vertex integrity are parameter-sized which can be always made bigger than constant-sized components.", upper_bound=LINEAR),
    ])
UpperBound(id="g8LSVx", fr=distanceTo(stars), to=treedepth, notes=[
    Note(id="rmLeo2", text="First, treedepth removes vertices of the modulator, remainder has treedepth $2$", upper_bound=LINEAR),
    ])
UpperBound(id="0mwDzZ", fr=distanceTo(complete), to=clique_cover_num, notes=[
    Note(id="bYybsT", text="We cover the $k$ vertices of the modulator by cliques of size $1$ and cover the remaining clique by another one.", upper_bound=LINEAR),
    ])
UpperBound(id="JtMcJB", fr=clique_cover_num, to=max_independent_set, notes=[
    Note(id="h8nG9p", text="Every clique of the clique cover partition may contain at most one vertex of the independent set.", upper_bound=LINEAR),
    ])
UpperBound(id="Fxp100", fr=max_independent_set, to=domination_num, notes=[
    Note(id="gGtTUf", text="Every maximal independent set is also a dominating set because any undominated vertex could be added to the independent set.", upper_bound=LINEAR),
    ])
UpperBound(id="UcXeli", fr=domination_num, to=diameter, notes=[
    Note(id="J0jyXi", text="An unbounded diameter implies a long path where no vertices that are more than $3$ apart may be dominated by the same dominating vertex, otherwise we could shorten the path. Hence, the number of dominating vertices is also unbounded.", upper_bound=LINEAR),
    ])
UpperBound(id="kXNdFI", fr=distanceTo(bipartite), to=chromatic_num, notes=[
    Note(id="xrVJqb", text="Removed vertices get one color each and we need only $2$ colors for the rest.", upper_bound=LINEAR),
    ])
UpperBound(id="YHgf7M", fr=average_degree, to=min_degree, notes=[
    definition
    ])
UpperBound(id="hTp0QP", fr=diameter, to=average_distance, notes=[
    definition
    ])
UpperBound(id="ySKjme", fr=max_matching, to=max_induced_matching, notes=[
    definition
    ])
UpperBound(id="cYFhiJ", fr=branch_width, to=treewidth, notes=[
    Cite(id="wrBAYk", url="https://en.wikipedia.org/wiki/Branch-decomposition", text="Relation to treewidth ... for a graph $G$ with tree-width $k$ and branchwidth $b > 1$, $b - 1 \\le k$ ...", upper_bound=LINEAR),
    ])
UpperBound(id="J94Xp2", fr=treewidth, to=branch_width, notes=[
    Cite(id="8ewSpI", url="https://en.wikipedia.org/wiki/Branch-decomposition", text="Relation to treewidth ... for a graph $G$ with tree-width $k$ and branchwidth $b > 1$, ... $k \\le \\lfloor \\frac 32 b \\rfloor - 1$", upper_bound=LINEAR),
    ])
UpperBound(id="paKd9Z", fr=rank_width, to=clique_width, notes=[
    Cite(id="yLdAHe", source=Oum2006, text="Proposition 6.3", upper_bound=EXPONENTIAL, known_tight=True),
    ])
UpperBound(id="zwiV6A", fr=clique_width, to=rank_width, notes=[
    Cite(id="uEUXMq", source=Oum2006, text="Proposition 6.3", upper_bound=LINEAR),
    ])
UpperBound(id="tSmPSE", fr=vertex_cover, to=neighborhood_diversity, notes=[
    Cite(id="YgTRtT", url="https://link.springer.com/article/10.1007/s00453-011-9554-x", text="Construct $k$ singleton sets, one for each vertex in the vertex cover and at most $2^k$ additional sets, one for each subset of vertices of the vertex cover. ...", upper_bound=EXPONENTIAL),
    ])
UpperBound(id="2f2OYD", fr=twin_cover_num, to=distanceTo(cluster), notes=[
    definition
    ])
UpperBound(id="7rSPl5", fr=vertex_cover, to=twin_cover_num, notes=[
    definition
    ])
#  UpperBound(id="rJOrPy", fr=distanceTo(complete), to=neighborhood_diversity, notes=[
    #  Cite(id="YgTRtT", url="https://link.springer.com/article/10.1007/s00453-011-9554-x", text="Construct $k$ singleton sets, one for each vertex in the vertex cover and at most $2^k$ additional sets, one for each subset of vertices of the vertex cover. ...", upper_bound=EXPONENTIAL),
    #  ])
UpperBound(id="Qkq8ZK", fr=edge_clique_cover, to=neighborhood_diversity, notes=[
    Note(id="5wc1ir", text="Label vertices by the cliques they are contained in, each label is its own group in the neighborhood diversity, connect accordingly.", upper_bound=EXPONENTIAL),
    ])
UpperBound(id="tN964P", fr=distanceTo(complete), to=edge_clique_cover, notes=[
    Note(id="RnkWvT", text="Cover the remaining clique, cover each modulator vertex and its neighborhood outside of it with another clique, cover each edge within the modulator by its own edge.", upper_bound=POLYNOMIAL),
    ])
UpperBound(id="APxeGN", fr=bandwidth, to=topological_bandwidth, notes=[
    definition
    ])
UpperBound(id="UXxQwz", fr=cutwidth, to=topological_bandwidth, notes=[])
UpperBound(id="UerLFp", fr=topological_bandwidth, to=pathwidth, notes=[])
UpperBound(id="2FIPpF", fr=treewidth, to=book_thickness, notes=[])
UpperBound(id="DjfbnG", fr=chromatic_num, to=chordality, notes=[])
UpperBound(id="ljoRXM", fr=boxicity, to=chordality, notes=[])
UpperBound(id="9HXBj6", fr=max_leaf_num, to=cutwidth, notes=[])
UpperBound(id="8oOsXL", fr=max_leaf_num, to=distanceTo(linear_forest), notes=[])
UpperBound(id="8JcAxM", fr=genus, to=book_thickness, notes=[])
UpperBound(id="JArOAD", fr=acyclic_chromatic_number, to=boxicity, notes=[])
UpperBound(id="2WpXNT", fr=acyclic_chromatic_number, to=degeneracy, notes=[])
UpperBound(id="pEPofm", fr=hindex, to=acyclic_chromatic_number, notes=[])
UpperBound(id="HqAvbm", fr=distanceTo(chordal), to=chordality, notes=[])
UpperBound(id="crL8y9", fr=distanceTo(cograph), to=clique_width, notes=[])
UpperBound(id="i55YHW", fr=distanceTo(cograph), to=chordality, notes=[])
UpperBound(id="MgB6sE", fr=distanceTo(cograph), to=diameter, notes=[])
UpperBound(id="1LfCs5", fr=book_thickness, to=acyclic_chromatic_number, notes=[])
UpperBound(id="pEHP0K", fr=distanceTo(planar), to=acyclic_chromatic_number, notes=[])
UpperBound(id="x9pao2", fr=average_distance, to=girth, notes=[])
UpperBound(id="v4djMN", fr=max_leaf_num, to=feedback_edge_set, notes=[])
UpperBound(id="gQqUuq", fr=max_induced_matching, to=diameter, notes=[])
UpperBound(id="uzK8uZ", fr=max_independent_set, to=max_induced_matching, notes=[])
UpperBound(id="oWACte", fr=treedepth, to=shrub_depth, notes=[])
UpperBound(id="QGZfvk", fr=inf_flip_width, to=rank_width, notes=[
    Cite(id="9DTyeJ", source=Torunczyk2023, text="For every graph $G$, we have $\\mathrm{rankwidth}(G) \\le 3 \\mathrm{fw}_\\infty(G)+1 ...", upper_bound=LINEAR),
    ])
UpperBound(id="CMxTVG", fr=rank_width, to=inf_flip_width, notes=[
    Cite(id="zYQZyB", source=Torunczyk2023, text="For every graph $G$, we have ... $3 \\mathrm{fw}_\\infty(G)+1 \\le O(2^{\\mathrm{rankwidth(G)}}).", upper_bound=EXPONENTIAL),
    ])
UpperBound(id="8H9ZS7", fr=twin_width, to=r_flip_width, notes=[
    Cite(id="OdbuZP", source=Torunczyk2023, text="Theorem 7.1. Fix $r \\in \\mathbb N$. For every graph $G$ of twin-width $d$ we have: $\\mathrm{fw}_r(G) \\le 2^d \\cdot d^{O(r)}.$", upper_bound=EXPONENTIAL),
    ])
UpperBound(id="urj73A", fr=inf_flip_width, to=r_flip_width, notes=[
    definition,
    ])
UpperBound(id="WxT333", fr=neighborhood_diversity, to=shrub_depth, notes=[])
UpperBound(id="1r3KyM", fr=twin_cover_num, to=shrub_depth, notes=[])
UpperBound(id="Tgla1H", fr=shrub_depth, to=linear_clique_width, notes=[])
UpperBound(id="knb7xY", fr=linear_clique_width, to=clique_width, notes=[])
UpperBound(id="WrPQkl", fr=clique_width, to=boolean_width, notes=[
    Note(id="OUUh3y", text="", upper_bound=LINEAR),
    ])
UpperBound(id="DYXpTJ", fr=boolean_width, to=clique_width, notes=[
    Note(id="hgUvsR", text="", upper_bound=EXPONENTIAL),
    ])
UpperBound(id="jDJD1a", fr=treewidth, to=boolean_width, notes=[
    Note(id="h8IR04", text="", upper_bound=LINEAR),
    ])
UpperBound(id="zTUpw7", fr=boolean_width, to=rank_width, notes=[
    Cite(id="AdNkCy", source=BuiXuan2011, text="\\textbf{Corollary 1.} For any graph $G$ and decomposition tree $(T,\\gamma)$ of $G$ it holds that ... $\\log_2 rw(G) \\le boolw(G)$ ...", upper_bound=EXPONENTIAL),
    ])
UpperBound(id="9gOugR", fr=rank_width, to=boolean_width, notes=[
    Cite(id="cIWQDn", source=BuiXuan2011, text="\\textbf{Corollary 1.} For any graph $G$ and decomposition tree $(T,\\gamma)$ of $G$ it holds that ... $boolw(G) \\le \\frac 14 rw^2(G)+O(rw(G))$.", upper_bound=POLYNOMIAL),
    ])
UpperBound(id="Q2HGHL", fr=branch_width, to=boolean_width, notes=[
    Note(id="V9Pisv", text="", upper_bound=LINEAR),
    ])
UpperBound(id="yczIfo", fr=branch_width, to=rank_width, notes=[
    Note(id="0zGd6N", text="", upper_bound=LINEAR),
    ])
UpperBound(id="OgRVGZ", fr=treewidth, to=boolean_width, notes=[])
UpperBound(id="3foRhH", fr=cutwidth, to=bandwidth, notes=[])
UpperBound(id="Ye2Rw9", fr=cutwidth, to=carvingwidth, notes=[])
UpperBound(id="5u1jOQ", fr=carvingwidth, to=max_degree, notes=[])
UpperBound(id="Gjs6EG", fr=carvingwidth, to=treewidth, notes=[])
UpperBound(id="daS9Eq", fr=twin_cover_num, to=modular_width, notes=[])
UpperBound(id="fPN7Hh", fr=neighborhood_diversity, to=modular_width, notes=[])
UpperBound(id="bAtfDb", fr=modular_width, to=clique_width, notes=[])
UpperBound(id="CGHBb7", fr=modular_width, to=diameter, notes=[])
UpperBound(id="PoU1Os", fr=neighborhood_diversity, to=boxicity, notes=[])
UpperBound(id="N1Tvo6", fr=genus, to=twin_width, notes=[])
UpperBound(id="Cu42bt", fr=distanceTo(planar), to=twin_width, notes=[])
UpperBound(id="osrMmj", fr=max_degree, to=c_closure, notes=[])
UpperBound(id="FSYBu2", fr=feedback_edge_set, to=c_closure, notes=[])


Equivalent("H1gQ6m", feedback_vertex_set, distanceTo(forest), [])
Equivalent("hDNUsi", vertex_cover, distanceTo(isolated), [])
Equivalent("8Mm5qJ", vertex_cover, max_matching, [
    Cite(id="gBA7dc", url="https://en.wikipedia.org/wiki/K%C5%91nig%27s_theorem_(graph_theory)", text="Kőnig's theorem"),
    ])
Equivalent("U14yX4", odd_cycle_transversal, distanceTo(bipartite), [
    Note(id="lqOY3G", text="Bipartite graphs is the graph class without any odd cycles."),
    ])


HasUnbounded(id="o3lQnF", graph_class=complete, parameter=treewidth, notes=[
    Note(id="cIAr80", text="Every clique appears whole in some bag of the treewidth decomposition."),
    ])
HasUnbounded(id="Jyi5e3", graph_class=complete, parameter=max_clique, notes=[])
HasUnbounded(id="t9mJyF", graph_class=complete, parameter=domatic_num, notes=[])
HasUnbounded(id="KnGxdS", graph_class=complete, parameter=edge_connectivity, notes=[])
HasUnbounded(id="fQjK7z", graph_class=co_cluster, parameter=distanceTo(chordal), notes=[])
HasBounded(id="cOXKlo", graph_class=cluster, parameter=twin_cover_num, notes=[])
HasUnbounded(id="WFO7PL", graph_class=cluster, parameter=neighborhood_diversity, notes=[])
HasUnbounded(id="jIxF3A", graph_class=cluster, parameter=domination_num, notes=[])
HasUnbounded(id="OjWb8I", graph_class=bipartite, parameter=girth, notes=[])
HasUnbounded(id="d1qoN7", graph_class=bipartite, parameter=edge_connectivity, notes=[])
HasBounded(id="Z335lf", graph_class=forest, parameter=feedback_edge_set, notes=[])
HasUnbounded(id="5pJxbA", graph_class=forest, parameter=girth, notes=[])
HasUnbounded(id="AdhtOR", graph_class=forest, parameter=pathwidth, notes=[])
#  HasUnbounded(id="k18Pyk", graph_class=forest, parameter=distanceTo(interval), notes=[])
HasBounded(id="2QZo3T", graph_class=isolated, parameter=vertex_cover, notes=[])
HasUnbounded(id="cq2q83", graph_class=isolated, parameter=domination_num, notes=[])
HasUnbounded(id="ipo6rm", graph_class=grid, parameter=clique_width, notes=[])
HasUnbounded(id="TOJxXi", graph_class=grid, parameter=distanceTo(chordal), notes=[])
HasUnbounded(id="MRucBP", graph_class=grid, parameter=average_distance, notes=[])
HasUnbounded(id="fQjK7z", graph_class=grid, parameter=max_degree, notes=[])
HasUnbounded(id="HOULS0", graph_class=cycles, parameter=girth, notes=[])
HasUnbounded(id="OjWb8I", graph_class=interval, parameter=average_distance, notes=[])
HasUnbounded(id="967lJ2", graph_class=linear_forest, parameter=treedepth, notes=[])
HasUnbounded(id="ne07p3", graph_class=linear_forest, parameter=average_distance, notes=[])
HasBounded(id="kkMeCO", graph_class=planar, parameter=genus, notes=[])
HasUnbounded(id="EZdonY", graph_class=planar, parameter=girth, notes=[])
HasUnbounded(id="cIAr80", graph_class=planar, parameter=max_degree, notes=[])
HasUnbounded(id="DxmXhS", graph_class=planar, parameter=distanceTo(perfect), notes=[])
HasBounded(id="QeiwSR", graph_class=const_components, parameter=cutwidth, notes=[])
HasUnbounded(id="EjGaM8", graph_class=const_components, parameter=distanceTo(perfect), notes=[])
HasUnbounded(id="bQLN2O", graph_class=const_components, parameter=distanceTo(planar), notes=[])
HasUnbounded(id="CoBOm0", graph_class=stars, parameter=hindex, notes=[])
HasUnbounded(id="I0yb6U", graph_class=stars, parameter=distanceTo(interval), notes=[])
HasUnbounded(id="Ei8B1H", graph_class=stars, parameter=vertex_integrity, notes=[])


#  ZHXKjC
#  PUSZhY
