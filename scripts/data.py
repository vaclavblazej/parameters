#!/usr/bin/env python3

import os
import sys

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb


def avg_color(color1, color2, weight):
    rgb1 = hex_to_rgb(color1)
    rgb2 = hex_to_rgb(color2)

    def avg(x, y, w):
        return round((x*(1-w)) + y*w)
    new_rgb = ()
    for i in range(len(rgb1)):
        new_rgb += (avg(rgb1[i], rgb2[i], weight),)
    return rgb_to_hex(new_rgb)


def check_type(x, tp):
    if 'type' not in x:
        return False
    return x['type']['!id'] == tp


def check_is_par(x):
    return check_type(x, '!TrvG50')

def check_is_connection(x):
    return check_type(x, '!jgWdIT')

def sas(e, a):
    return f'{a} = {e.attr(a)}'

class CustomType:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

class Entry:
    def __init__(self, id, name, abbreviation, hue, notes):
        self.id = id
        self.name = name
        self.abbreviation = abbreviation
        self.hue = hue
        self.notes = notes

    def __str__(self):
        notes = ',\n'.join(list(map(str,self.notes)))
        return f'Entry(id = "{self.id}", name = "{self.name}", abbreviation = "{self.abbreviation}", hue = {self.hue}, notes = [\n{notes}\n])'

class UpperBound:
    def __init__(self, id, fr, to, notes):
        self.id = id
        self.fr = fr
        self.to = to
        self.notes = notes

    def __str__(self):
        notes = ',\n'.join(list(map(str,self.notes)))
        return f'UpperBound(id = "{self.id}", fr = {self.fr}, to = {self.to}, notes = [\n{notes}\n])'

class Notes:
    def __init__(self, e):
        self.id = e['!id']
        self.url = None
        if 'url' in e:
            self.url = e['url']
        self.text = e['text']

    def __str__(self):
        return f'Note(id = "{self.id}", url = "{self.url}", text = "{self.text}")'

class Note:
    def __init__(self, id, url, text):
        self.id = id
        self.url = url
        self.text = text

    def __str__(self):
        return f'Note(id = "{self.id}", url = "{self.url}", text = "{self.text}")'

parameter_type = CustomType(
        id = "!TrvG50",
        name = "parameter",
        description = "Instance of this type represents a graph Parameter in the context of Parameterized complexity. They are associated with meta-data, e.g., an approximate (and highly oppinionated) importance, and upper_bounds that says whether for this parameter $k$ and any graph there is a computable function $f$ such that another parameter is upper bound by $f(k)$."
        )

bound_type = CustomType(
        id = "!jgWdIT",
        name = "upper bounds",
        description = "Connection between two parameters that describes that if the first one is K then the second one is at most f(K) where f is a computable function. Alternatively, one can think about this relation as that the second one is potentially smaller for a wider class of graphs"
        )

treewidth = Entry(id = "!IcKqSn", name = "treewidth", abbreviation = None, hue = 1, notes = [
    Note(id = "!W4j934", url = "https://en.wikipedia.org/wiki/Treewidth", text = "..., the treewidth of an undirected graph is an integer number which specifies, informally, how far the graph is from being a tree."),
    Note(id = "!xnhT1P", url = "https://www.mimuw.edu.pl/~malcin/book/parameterized-algorithms.pdf", text = "Very roughly, treewidth captures how similar a graph is to a tree. There are many ways to define ``tree-likeness'' of a graph; ... it appears that the approach most useful from algorithmic and graph theoretical perspectives, is to view tree-likeness of a graph $G$ as the existence of a structural decomposition of $G$ into pieces of bounded size that are connected in a tree-like fashion. This intuitive concept is formalized via the notions of a *tree decomposition* and the *treewidth* of a graph; the latter is a quantitative measure of how good a tree decomposition we can possibly obtain.")
    ])
pathwidth = Entry(id = "!nQhAoF", name = "pathwidth", abbreviation = None, hue = 0.9, notes = [
    Note(id = "!dxaIhi", url = "https://mathworld.wolfram.com/Pathwidth.html", text = "The pathwidth of a graph $G$, also called the interval thickness, vertex separation number, and node searching number, is one less than the size of the largest set in a path decomposition G.")
    ])
treedepth = Entry(id = "!KEP2qM", name = "treedepth", abbreviation = None, hue = 0.9, notes = [
    Note(id = "!QHJ1Kl", url = "https://en.wikipedia.org/wiki/Tree-depth", text = "The tree-depth of a graph $G$ may be defined as the minimum height of a forest $F$ with the property that every edge of $G$ connects a pair of nodes that have an ancestor-descendant relationship to each other in $F$.")
    ])
fvs = Entry(id = "!GNOiyB", name = "feedback vertex set", abbreviation = None, hue = 0.9, notes = [
    Note(id = "!BJhqpe", url = "https://en.wikipedia.org/wiki/Feedback_vertex_set", text = "... a feedback vertex set (FVS) of a graph is a set of vertices whose removal leaves a graph without cycles... . The feedback vertex set number of a graph is the size of a smallest feedback vertex set."),
    Note(id = "!81zlqB", url = None, text = "can be thought of as a *distance to forest*")
    ])
fes = Entry(id = "!HTk9PZ", name = "feedback edge set", abbreviation = None, hue = 0.7, notes = [
    Note(id = "!WP7pFA", url = "https://stackoverflow.com/questions/10791689/how-to-find-feedback-edge-set-in-undirected-graph", text = "Let $G = (V,E)$ be an undirected graph. A set $F \subseteq E$ of edges is called a feedback-edge set if every cycle of $G$ has at least one edge in $F$.")
    ])
vc = Entry(id = "!4lp9Yj", name = "vertex cover", abbreviation = None, hue = 1, notes = [
    Note(id = "!ez07Er", url = "https://en.wikipedia.org/wiki/Vertex_cover", text = "... set of vertices that includes at least one endpoint of every edge of the graph."),
    Note(id = "!DFiBbf", url = None, text = "can be thought of as a *distance to independent set*")
    ])
cliquewidth = Entry(id = "!U3jPaT", name = "cliquewidth", abbreviation = None, hue = 0.8, notes = [
    Note(id = "!9Ckusi", url = "https://en.wikipedia.org/wiki/Clique-width", text = "... the minimum number of labels needed to construct G by means of the following 4 operations: 1. Creation of a new vertex... 2. Disjoint union of two labeled graphs... 3. Joining by an edge every vertex labeled $i$ to every vertex labeled $j$, where $i \ne j$ 4. Renaming label $i$ to label $j$")
    ])
chromatic_num = Entry(id = "!MB1Sr1", name = "chromatic number", abbreviation = None, hue = 0.2, notes = [
    Note(id = "!VqwUmp", url = "https://mathworld.wolfram.com/ChromaticNumber.html", text = "The chromatic number of a graph G is the smallest number of colors needed to color the vertices of G so that no two adjacent vertices share the same color (Skiena 1990, p. 210), ...")
    ])
degeneracy = Entry(id = "!m2q96O", name = "degeneracy", abbreviation = None, hue = 0.2, notes = [
    Note(id = "!6LCwBu", url = "https://en.wikipedia.org/wiki/Degeneracy_(graph_theory)", text = "... the least $k$ for which there exists an ordering of the vertices of $G$ in which each vertex has fewer than $k$ neighbors that are earlier in the ordering.")
    ])
genus = Entry(id = "!gbaHdw", name = "genus", abbreviation = None, hue = 0.3, notes = [
    Note(id = "!8ryhNq", url = "https://en.wikipedia.org/wiki/Genus_(mathematics)#Graph_theory", text = "The genus of a graph is the minimal integer $n$ such that the graph can be drawn without crossing itself on a sphere with $n$ handles.")
    ])
boxicity = Entry(id = "!j1rrOV", name = "boxicity", abbreviation = None, hue = 0.2, notes = [
    Note(id = "!XWbXPm", url = "https://en.wikipedia.org/wiki/Boxicity", text = "The boxicity of a graph is the minimum dimension in which a given graph can be represented as an intersection graph of axis-parallel boxes.")
    ])
max_degree = Entry(id = "!UyQ5yM", name = "maximum degree", abbreviation = None, hue = 0.4, notes = [
    Note(id = "!8tk4SI", url = None, text = "maximum degree of graph's vertices")
    ])
min_degree = Entry(id = "!NCg08F", name = "minimum degree", abbreviation = None, hue = 0.1, notes = [
    Note(id = "!CKNuj2", url = None, text = "minimum degree of graph's vertices")
    ])
acn = Entry(id = "!QoA8jA", name = "acyclic chromatic number", abbreviation = None, hue = 0.3, notes = [
    Note(id = "!cNSdgE", url = "https://www.graphclasses.org/classes/par_31.html", text = "The acyclic chromatic number of a graph $G$ is the smallest size of a vertex partition $V_1,\dots,V_\ell$ such that each $V_i$ is an independent set and for all $i,j$ that graph $G[V_i \cup V_j]$ does not contain a cycle."),
    Note(id = "!rj2m4h", url = "https://en.wikipedia.org/wiki/Acyclic_coloring", text = "... an acyclic coloring is a (proper) vertex coloring in which every 2-chromatic subgraph is acyclic.")
    ])
hindex = Entry(id = "!gKbGUa", name = "h-index", abbreviation = None, hue = 0.1, notes = [
    Note(id = "!WY6oNX", url = "https://link.springer.com/chapter/10.1007/978-3-642-03367-4_25", text = "... $h$ is the $h$-index of the graph, the maximum number such that the graph contains $h$ vertices of degree at least $h$.")
    ])
bandwidth = Entry(id = "!aP5a38", name = "bandwidth", abbreviation = None, hue = 0.4, notes = [
    Note(id = "!s7OvjQ", url = "https://en.wikipedia.org/wiki/Graph_bandwidth", text = "(paraphrased) Label graph vertices with distinct integers. Bandwidth of this labelling is the maximum over label differences over all edges. Bandwidth of a graph is the minimum over all labellings.")
    ])
bisection_bandwidth = Entry(id = "!wUdmUb", name = "bisection bandwidth", abbreviation = None, hue = 0.3, notes = [
    Note(id = "!iWUynL", url = "https://en.wikipedia.org/wiki/Bisection_bandwidth", text = "... bisected into two equal-sized partitions, the bisection bandwidth of a network topology is the bandwidth available between the two partitions."),
    Note(id = "!AeRM2B", url = "http://parallelcomp.github.io/Lecture3.pdf", text = "[number of] links across smallest cut that divides nodes in two (nearly) equal parts")
    ])
max_leaf_num = Entry(id = "!BN92vX", name = "maximum leaf number", abbreviation = None, hue = 0.3, notes = [
    Note(id = "!Q3HJs5", url = "https://mathworld.wolfram.com/MaximumLeafNumber.html", text = "... the largest number of tree leaves in any of its spanning trees.")
    ])
dist_lin_forest = Entry(id = "!9XDQCE", name = "distance to linear forest", abbreviation = None, hue = 0.6, notes = [
    Note(id = "!MBBkVW", url = None, text = "We can remove $k$ vertices to obtain a graph from the graph class mentioned in name of this parameter.")
    ])
dist_cycles = Entry(id = "!599Nkv", name = "distance to trees and disjoint cycles", abbreviation = None, hue = 0.1, notes = [
    Note(id = "!MBBkVW", url = None, text = "We can remove $k$ vertices to obtain a graph from the graph class mentioned in name of this parameter.")
    ])
dist_cluster = Entry(id = "!TzspYl", name = "distance to cluster", abbreviation = None, hue = 0.7, notes = [
    Note(id = "!MBBkVW", url = None, text = "We can remove $k$ vertices to obtain a graph from the graph class mentioned in name of this parameter.")
    ])
dist_interval = Entry(id = "!rr2exi", name = "distance to interval", abbreviation = None, hue = 0.3, notes = [
    Note(id = "!MBBkVW", url = None, text = "We can remove $k$ vertices to obtain a graph from the graph class mentioned in name of this parameter.")
    ])
dist_chordal = Entry(id = "!oi8KhK", name = "distance to chordal", abbreviation = None, hue = 0.3, notes = [
    Note(id = "!MBBkVW", url = None, text = "We can remove $k$ vertices to obtain a graph from the graph class mentioned in name of this parameter.")
    ])
dist_outerplanar = Entry(id = "!ThJdP1", name = "distance to outerplanar", abbreviation = None, hue = 0.5, notes = [
    Note(id = "!MBBkVW", url = None, text = "We can remove $k$ vertices to obtain a graph from the graph class mentioned in name of this parameter.")
    ])
dist_cograph = Entry(id = "!QiDXEo", name = "distance to cograph", abbreviation = None, hue = 0.2, notes = [
    Note(id = "!MBBkVW", url = None, text = "We can remove $k$ vertices to obtain a graph from the graph class mentioned in name of this parameter.")
    ])
dist_const = Entry(id = "!bRBb5K", name = "distance to constant components", abbreviation = None, hue = 0.3, notes = [
    Note(id = "!MBBkVW", url = None, text = "We can remove $k$ vertices to obtain a graph from the graph class mentioned in name of this parameter.")
    ])
vertex_integrity = Entry(id = "!KVhJFB", name = "vertex integrity", abbreviation = None, hue = 0.5, notes = [
    Note(id = "!aQQnbF", url = None, text = "Minimum $k$ such that there exists $k$ vertices whose removal results in connected components of sizes at most $k$.")
    ])
dist_stars = Entry(id = "!PwPrlq", name = "distance to stars", abbreviation = None, hue = 0.2, notes = [
    Note(id = "!MBBkVW", url = None, text = "We can remove $k$ vertices to obtain a graph from the graph class mentioned in name of this parameter.")
    ])
chordality = Entry(id = "!fTqo40", name = "chordality", abbreviation = None, hue = 0.8, notes = [
    Note(id = "!zYzUJ5", url = "https://onlinelibrary.wiley.com/doi/abs/10.1002/jgt.3190170210", text = "The \emph{chordality} of a graph $G=(V,E)$ is defined as the minimum $k$ such that we can write $E=E_1,\cap\dots\cap E_k$ with each $(V,E_i)$ a chordal graph.")
    ])
dist_clique = Entry(id = "!7ugOaW", name = "distance to clique", abbreviation = None, hue = 0.3, notes = [
    Note(id = "!MBBkVW", url = None, text = "We can remove $k$ vertices to obtain a graph from the graph class mentioned in name of this parameter.")
    ])
clique_cover_num = Entry(id = "!VomShB", name = "clique cover number", abbreviation = None, hue = 0.5, notes = [
    Note(id = "!jh0OIZ", url = "https://en.wikipedia.org/wiki/Clique_cover", text = "A minimum clique cover is a clique cover that uses as few cliques as possible. The minimum $k$ for which a clique cover exists is called the clique cover number of the given graph.")
    ])
max_independent_set = Entry(id = "!mHtXUU", name = "maximum independent set", abbreviation = None, hue = 0.9, notes = [
    Note(id = "!0cYayY", url = "https://en.wikipedia.org/wiki/Maximal_independent_set", text = "For a graph $G=(V,E)$, an independent set $S$ is a maximal independent set if for $v \in V$, one of the following is true: 1) $v \in S$ 2), $N(v) \cap S \ne \emptyset$ where $N(v)$ denotes the neighbors of $v$. ... the largest maximum independent set of a graph is called a maximum independent set.")
])
domination_num = Entry(id = "!Gq0onN", name = "domination number", abbreviation = None, hue = 1, notes = [
    Note(id = "!82RsGb", url = "https://mathworld.wolfram.com/DominationNumber.html", text = "The domination number $\gamma(G)$ of a graph $G$ is the minimum size of a dominating set of vertices in $G$ ...")
    ])
girth = Entry(id = "!AxyLAU", name = "girth", abbreviation = None, hue = 1, notes = [
    Note(id = "!u13WN1", url = "https://en.wikipedia.org/wiki/Girth_(graph_theory)", text = "In graph theory, the girth of an undirected graph is the length of a shortest cycle contained in the graph.")
    ])
dist_bipartite = Entry(id = "!T9s5sR", name = "distance to bipartite", abbreviation = None, hue = 0.4, notes = [
    Note(id = "!MBBkVW", url = None, text = "We can remove $k$ vertices to obtain a graph from the graph class mentioned in name of this parameter.")
    ])
dist_perfect = Entry(id = "!TLdoEo", name = "distance to perfect", abbreviation = None, hue = 0.2, notes = [
    Note(id = "!MBBkVW", url = None, text = "We can remove $k$ vertices to obtain a graph from the graph class mentioned in name of this parameter.")
    ])
max_clique = Entry(id = "!zYkYWx", name = "maximum clique", abbreviation = None, hue = 0.7, notes = [
    Note(id = "!PVi4lL", url = "https://mathworld.wolfram.com/MaximumClique.html", text = "A maximum clique of a graph $G$ is a clique (i.e., complete subgraph) of maximum possible size for $G$.")
    ])
average_degree = Entry(id = "!X7CxTe", name = "average degree", abbreviation = None, hue = 0.4, notes = [
    Note(id = "!o6tFCJ", url = "https://bookdown.org/omarlizardo/_main/2-7-average-degree.html", text = "Average degree is simply the average number of edges per node in the graph. ... Total Edges/Total Nodes=Average Degree")
    ])
domatic_num = Entry(id = "!KRV6tI", name = "domatic number", abbreviation = None, hue = 0.3, notes = [
    Note(id = "!8eXjAy", url = "https://mathworld.wolfram.com/DomaticNumber.html", text = "The maximum number of disjoint dominating sets in a domatic partition of a graph $G$ is called its domatic number $d(G)$. ")
    ])
vertex_connectivity = Entry(id = "!CIEnCh", name = "vertex connectivity / distance to disconnected", abbreviation = None, hue = 0.5, notes = [
    Note(id = "!MBBkVW", url = None, text = "We can remove $k$ vertices to obtain a graph from the graph class mentioned in name of this parameter.")
    ])
twinwidth = Entry(id = "!VipBQc", name = "twinwidth", abbreviation = None, hue = 0.6, notes = [
    Note(id = "!nyaOye", url = "https://dl.acm.org/doi/10.1145/3486655", text = "... we consider a sequence of graph $G_n,G_{n-1},\dots,G_2,G_1$, where $G_n$ is the original graph $G$, $G_1$ is the one-vertex graph, $G_i$ has $i$ vertices, and $G_{i-1}$ is obtained from $G_i$ by performing a single contraction of two (non-necessarily adjacent) vertices. For every vertex $u \in V(G_i)$, let us denote by $u(G)$ the vertices of $G$ which have been contracted to $u$ along the sequence $G_n,\dots,G_i$. A pair of disjoint sets of vertices is homogeneous if, between these sets, there are either all possible edges or no edge at all. The red edges mentioned previously consist of all pairs $uv$ of vertices of $G_i$ such that $u(G)$ and $v(G)$ are not homogeneous in $G$. If the red degree of every $G_i$ is at most $d$, then $G_n,G_{n-1},\dots,G_2,G_1$ is called a sequence of $d$-contractions, or $d$-sequence. The twin-width of $G$ is the minimum $d$ for which there exists a sequence of $d$-contractions.")
    ])
book_thickness = Entry(id = "!pKMM6O", name = "book thickness", abbreviation = None, hue = 0.3, notes = [
    Note(id = "!YGmwCG", url = "https://en.wikipedia.org/wiki/Book_embedding", text = "... a book embedding is a generalization of planar embedding of a graph to embeddings into a book, a collection of half-planes all having the same line as their boundary. Usually, the vertices of the graph are required to lie on this boundary line, called the spine, and the edges are required to stay within a single half-plane. The book thickness of a graph is the smallest possible number of half-planes for any book embedding of the graph.")
    ])
dist_planar = Entry(id = "!3Xj5rP", name = "distance to planar", abbreviation = None, hue = 0.3, notes = [
    Note(id = "!MBBkVW", url = None, text = "We can remove $k$ vertices to obtain a graph from the graph class mentioned in name of this parameter.")
    ])
diameter = Entry(id = "!QF9fW9", name = "diameter", abbreviation = None, hue = 0.2, notes = [
    Note(id = "!055mG5", url = "https://en.wikipedia.org/wiki/Distance_(graph_theory)#Related_concepts", text = "... [diameter] is the greatest distance between any pair of vertices ...")
    ])
average_distance = Entry(id = "!GPmPOT", name = "average distance", abbreviation = None, hue = 0.1, notes = [
    Note(id = "!GfSsR4", url = "https://onlinelibrary.wiley.com/doi/abs/10.1002/jgt.3190120309", text = "The average distance in a graph is defined as the average length of a shortest path between two vertices, taken over all pairs of vertices.")
    ])
max_induced_matching = Entry(id = "!wpeKEI", name = "maximum induced matching", abbreviation = None, hue = 0.3, notes = [
    Note(id = "!TKnuNP", url = "https://www.sciencedirect.com/science/article/pii/0166218X9290275F?via%3Dihub", text = "An induced matching in a graph G is a set of edges, no two of which meet a common node or are joined by an edge of G;")
    ])
max_matching = Entry(id = "!veU7Jf", name = "maximum matching", abbreviation = None, hue = 0.6, notes = [
    Note(id = "!f3q99d", url = "https://www.graphclasses.org/classes/par_13.html", text = "A matching in a graph is a subset of pairwise disjoint edges (any two edges that do not share an endpoint). The parameter maximum matching of a graph $G$ is the largest size of a matching in $G$.")
    ])
branch_width = Entry(id = "!W0Iwpj", name = "branch width", abbreviation = None, hue = 0.5, notes = [
    Note(id = "!ZhBkjd", url = "https://en.wikipedia.org/wiki/Branch-decomposition", text = "... branch-decomposition of an undirected graph $G$ is a hierarchical clustering of the edges of $G$, represented by an unrooted binary tree $T$ with the edges of $G$ as its leaves. Removing any edge from $T$ partitions the edges of $G$ into two subgraphs, and the width of the decomposition is the maximum number of shared vertices of any pair of subgraphs formed in this way. The branchwidth of $G$ is the minimum width of any branch-decomposition of $G$.")
    ])
rank_width = Entry(id = "!IMmY3n", name = "rank-width", abbreviation = None, hue = 0.5, notes = [
    Note(id = "!pjVGlR", url = "https://www.sciencedirect.com/science/article/pii/S0095895605001528", text = "see Section 6")
    ])
edge_connectivity = Entry(id = "!W3n2Jv", name = "edge connectivity", abbreviation = None, hue = 0.7, notes = [
    Note(id = "!ZunX1e", url = "https://mathworld.wolfram.com/EdgeConnectivity.html", text = "The edge connectivity, also called the line connectivity, of a graph is the minimum number of edges $\lambda(G)$ whose deletion from a graph $G$ disconnects $G$.")
    ])
neighborhood_diversity = Entry(id = "!vMs3RS", name = "neighborhood diversity", abbreviation = None, hue = 0.6, notes = [
    Note(id = "!L2KX25", url = "https://link.springer.com/article/10.1007/s00453-011-9554-x", text = "We will say that two vertices $v, v'$ of a graph $G(V, E)$ have the same *type* iff they have the same colors and $N(v) \setminus \{v\} = N(v') \setminus \{v\}$, where $N(v)$ denotes the set of neighbors of $v$. ... A colored graph $G(V, E)$ has neighborhood diversity at most $w$, if there exists a partition of $V$ into at most $w$ sets, such that all the vertices in each set have the same type.")
    ])
shrub_depth = Entry(id = "!mOq1g7", name = "shrub-depth", abbreviation = None, hue = 0.4, notes = [
    Note(id = "!4Dua5N", url = "https://www.fi.muni.cz/~hlineny/papers/shrubdepth-warw18-slipp.pdf", text = "Tree-model of $m$ colors and depth $d$: a rooted tree $T$ of height $d$, leaves are the vertices of $G$, each leaf has one of $m$ colors, an associated signature determining the edge set of $G$ as follows: for $i = 1,2,\dots,d$, let $u$ and $v$ be leaves with the least common ancestor at height $i$ in $T$, then $uv \in E(G)$ iff the color pair of $u,v$ is in the signature at height $i$.")
    ])
twin_cover_num = Entry(id = "!MUnHA0", name = "twin cover number", abbreviation = None, hue = 0.4, notes = [
    Note(id = "!nTIDMU", url = None, text = "Distance to cluster where all vertices of each clique are siblings.")
    ])


entries = [
    treewidth,
    pathwidth,
    treedepth,
    fvs,
    fes,
    vc,
    cliquewidth,
    chromatic_num,
    degeneracy,
    genus,
    boxicity,
    max_degree,
    min_degree,
    acn,
    hindex,
    bandwidth,
    bisection_bandwidth,
    max_leaf_num,
    dist_lin_forest,
    dist_cycles,
    dist_cluster,
    dist_interval,
    dist_chordal,
    dist_outerplanar,
    dist_cograph,
    dist_const,
    vertex_integrity,
    dist_stars,
    chordality,
    dist_clique,
    clique_cover_num,
    max_independent_set,
    domination_num,
    girth,
    dist_bipartite,
    dist_perfect,
    max_clique,
    average_degree,
    domatic_num,
    vertex_connectivity,
    twinwidth,
    book_thickness,
    dist_planar,
    diameter,
    average_distance,
    max_induced_matching,
    max_matching,
    branch_width,
    rank_width,
    edge_connectivity,
    neighborhood_diversity,
    shrub_depth,
    twin_cover_num
]

connections = [
UpperBound(id = "!9V7MFq", fr = treewidth, to = cliquewidth, notes = [
    Note(id = "!DKZYEb", url = None, text = "A nice tree decomposition yields a clique width decomposition of bounded number of labels as the forgotten vertices get one color and bag vertices get each its own color.")
    ]),
UpperBound(id = "!2FIPpF", fr = treewidth, to = book_thickness, notes = []),
UpperBound(id = "!c7lkhf", fr = pathwidth, to = treewidth, notes = [
    Note(id = "!DQzjIV", url = None, text = "By definition. One parameter is special case of the other.")
    ]),
UpperBound(id = "!tKCHeJ", fr = treedepth, to = pathwidth, notes = [
    Note(id = "!q3qJkr", url = None, text = "Saving the set of open vertices in a DFS over the tree treedepth after every step yields bags of a nice path decomposition.")
    ]),
UpperBound(id = "!6Kl5Pp", fr = treedepth, to = diameter, notes = [
    Note(id = "!7tFsi6", url = None, text = "An unbounded diameter implies the class contains paths as subgraphs. Minimum treedepth to embed a path of length $n$ in a treedepth tree is $\log n$.")
    ]),
UpperBound(id = "!XqzgTC", fr = fvs, to = dist_chordal, notes = [
    Note(id = "!UQLQ2Q", url = None, text = "By graph inclusion of the remaining graph classes.")
    ]),
UpperBound(id = "!AbAK8n", fr = fvs, to = dist_bipartite, notes = [
    Note(id = "!nreA0R", url = None, text = "A.k.a. odd cycle transversal"),
    Note(id = "!UQLQ2Q", url = None, text = "By graph inclusion of the remaining graph classes.")
    ]),
UpperBound(id = "!slhzot", fr = fvs, to = dist_outerplanar, notes = [
    Note(id = "!UQLQ2Q", url = None, text = "By graph inclusion of the remaining graph classes.")
    ]),
UpperBound(id = "!XuYoYh", fr = fvs, to = dist_cycles, notes = [
    Note(id = "!UQLQ2Q", url = None, text = "By graph inclusion of the remaining graph classes.")
    ]),
UpperBound(id = "!9Pdp4G", fr = fes, to = fvs, notes = [
    Note(id = "!aQyAEM", url = None, text = "by a simple observation")
    ]),
UpperBound(id = "!12cxS9", fr = fes, to = genus, notes = [
    Note(id = "!8dQ8Us", url = None, text = "Removing $k$ edges creates a forest that is embeddable into the plane. We now add one handle for each of the $k$ edges to get embedding into $k$-handle genus.")
    ]),
UpperBound(id = "!BWJDZs", fr = vc, to = dist_stars, notes = [
    Note(id = "!UQLQ2Q", url = None, text = "By graph inclusion of the remaining graph classes.")
    ]),
UpperBound(id = "!VsrnoK", fr = vc, to = dist_lin_forest, notes = [
    Note(id = "!UQLQ2Q", url = None, text = "By graph inclusion of the remaining graph classes.")
    ]),
UpperBound(id = "!yWSq1V", fr = vc, to = dist_const, notes = [
    Note(id = "!UQLQ2Q", url = None, text = "By graph inclusion of the remaining graph classes.")
    ]),
UpperBound(id = "!5z03w7", fr = cliquewidth, to = twinwidth, notes = [
    Note(id = "!08lETp", url = None, text = "Once two vertices have the same label they share their neighborhood with respect to all vertices they are connected to further. So to get a twinwidth sequence we merge all vertices that get same labels. Hence, red edges may occur only between different labels and the maximum red degree is bounded by the number of labels.")
    ]),
UpperBound(id = "!juphuT", fr = chromatic_num, to = max_clique, notes = [
    Note(id = "!aQyAEM", url = None, text = "by a simple observation")
    ]),
UpperBound(id = "!DjfbnG", fr = chromatic_num, to = chordality, notes = []),
UpperBound(id = "!P4jZlH", fr = degeneracy, to = chromatic_num, notes = [
    Note(id = "!uKFrrb", url = None, text = "Greedily color the vertices in order of the degeneracy ordering. As each vertex has at most $k$ colored predecesors we use at most $k+1$ colors.")
    ]),
UpperBound(id = "!ncjZd0", fr = degeneracy, to = average_degree, notes = [
    Note(id = "!aQyAEM", url = None, text = "by a simple observation")
    ]),
UpperBound(id = "!8JcAxM", fr = genus, to = book_thickness, notes = []),
UpperBound(id = "!ljoRXM", fr = boxicity, to = chordality, notes = []),
UpperBound(id = "!PTu5gn", fr = max_degree, to = hindex, notes = [
    Note(id = "!aQyAEM", url = None, text = "by a simple observation")
    ]),
UpperBound(id = "!9uKn16", fr = min_degree, to = edge_connectivity, notes = [
    Note(id = "!aQyAEM", url = None, text = "by a simple observation")
    ]),
UpperBound(id = "!l4bNpX", fr = min_degree, to = domatic_num, notes = [
    Note(id = "!UYpwYn", url = None, text = "The vertex of minimum degree needs to be dominated in each of the sets. As the sets cannot overlap there can be at most $k+1$ of them.")
    ]),
UpperBound(id = "!JArOAD", fr = acn, to = boxicity, notes = []),
UpperBound(id = "!2WpXNT", fr = acn, to = degeneracy, notes = []),
UpperBound(id = "!pEPofm", fr = hindex, to = acn, notes = []),
UpperBound(id = "!v6d2P7", fr = bandwidth, to = pathwidth, notes = [
    Note(id = "!kiza4J", url = None, text = "Having bandwidth $k$, order vertices by their values. We create a bag for each vertex $u$ by taking $u$ and all vertices that have a value that is at most $k$ larger than the value of $u$. All edges fall into some bag and vertices span connected span of bags.")
    ]),
UpperBound(id = "!e6NaBr", fr = bandwidth, to = max_degree, notes = [
    Note(id = "!waxvtz", url = None, text = "Each vertex has an integer $i$ and may be connected only to vertices whose difference from $i$ is at most $k$. There are at most $k$ bigger and $k$ smaller such neighbors.")
    ]),
UpperBound(id = "!MKUFA8", fr = bandwidth, to = bisection_bandwidth, notes = [
    Note(id = "!LyJWeW", url = None, text = "Order vertices by their bandwidth integer. We split the graph in the middle of this ordering. There are at most roughly $k^2/2$ edges over this split.")
    ]),
UpperBound(id = "!sMfXRo", fr = bisection_bandwidth, to = edge_connectivity, notes = [
    Note(id = "!DQzjIV", url = None, text = "By definition. One parameter is special case of the other.")
    ]),
UpperBound(id = "!mgFizL", fr = max_leaf_num, to = bandwidth, notes = []),
UpperBound(id = "!8oOsXL", fr = max_leaf_num, to = dist_lin_forest, notes = []),
UpperBound(id = "!lmKGuy", fr = dist_lin_forest, to = fvs, notes = [
    Note(id = "!UQLQ2Q", url = None, text = "By graph inclusion of the remaining graph classes.")
    ]),
UpperBound(id = "!rHotfs", fr = dist_lin_forest, to = dist_interval, notes = [
    Note(id = "!UQLQ2Q", url = None, text = "By graph inclusion of the remaining graph classes.")
    ]),
UpperBound(id = "!KtFhkk", fr = dist_lin_forest, to = pathwidth, notes = [
    Note(id = "!d2ZJIh", url = None, text = "After removal of $k$ vertices the remaining class has a bounded width $w$. So by including the removed vertices in every bag, we can achieve decomposition of width $w+k$")
    ]),
UpperBound(id = "!150N9P", fr = dist_lin_forest, to = hindex, notes = [
    Note(id = "!d2ZJIh", url = None, text = "After removal of $k$ vertices the remaining class has a bounded width $w$. So by including the removed vertices in every bag, we can achieve decomposition of width $w+k$")
    ]),
UpperBound(id = "!B9l0ai", fr = dist_cycles, to = treewidth, notes = [
    Note(id = "!d2ZJIh", url = None, text = "After removal of $k$ vertices the remaining class has a bounded width $w$. So by including the removed vertices in every bag, we can achieve decomposition of width $w+k$")
    ]),
UpperBound(id = "!FM1wVJ", fr = dist_cluster, to = dist_interval, notes = [
    Note(id = "!UQLQ2Q", url = None, text = "By graph inclusion of the remaining graph classes.")
    ]),
UpperBound(id = "!7RXwqI", fr = dist_cluster, to = dist_cograph, notes = [
    Note(id = "!DQzjIV", url = None, text = "By definition. One parameter is special case of the other.")
    ]),
UpperBound(id = "!fKpyMg", fr = dist_interval, to = dist_chordal, notes = [
    Note(id = "!UQLQ2Q", url = None, text = "By graph inclusion of the remaining graph classes.")
    ]),
UpperBound(id = "!hKjhJE", fr = dist_interval, to = boxicity, notes = [
    Note(id = "!DQzjIV", url = None, text = "By definition. One parameter is special case of the other.")
    ]),
UpperBound(id = "!piRTZw", fr = dist_chordal, to = dist_perfect, notes = [
    Note(id = "!UQLQ2Q", url = None, text = "By graph inclusion of the remaining graph classes.")
    ]),
UpperBound(id = "!HqAvbm", fr = dist_chordal, to = chordality, notes = []),
UpperBound(id = "!voVCvr", fr = dist_outerplanar, to = treewidth, notes = [
    Note(id = "!d2ZJIh", url = None, text = "After removal of $k$ vertices the remaining class has a bounded width $w$. So by including the removed vertices in every bag, we can achieve decomposition of width $w+k$")
    ]),
UpperBound(id = "!ZiCzGe", fr = dist_outerplanar, to = dist_planar, notes = [
    Note(id = "!UQLQ2Q", url = None, text = "By graph inclusion of the remaining graph classes.")
    ]),
UpperBound(id = "!stwHRi", fr = dist_cograph, to = dist_perfect, notes = [
    Note(id = "!UQLQ2Q", url = None, text = "By graph inclusion of the remaining graph classes.")
    ]),
UpperBound(id = "!crL8y9", fr = dist_cograph, to = cliquewidth, notes = []),
UpperBound(id = "!i55YHW", fr = dist_cograph, to = chordality, notes = []),
UpperBound(id = "!MgB6sE", fr = dist_cograph, to = diameter, notes = []),
UpperBound(id = "!wKsJTT", fr = dist_const, to = vertex_integrity, notes = [
    Note(id = "!UQLQ2Q", url = None, text = "By graph inclusion of the remaining graph classes.")
    ]),
UpperBound(id = "!10tIHQ", fr = vertex_integrity, to = treedepth, notes = [
    Note(id = "!aQyAEM", url = None, text = "by a simple observation")
    ]),
UpperBound(id = "!g8LSVx", fr = dist_stars, to = treedepth, notes = [
    Note(id = "!aQyAEM", url = None, text = "by a simple observation")
    ]),
UpperBound(id = "!Tr2Ih9", fr = dist_clique, to = dist_cluster, notes = [
    Note(id = "!DQzjIV", url = None, text = "By definition. One parameter is special case of the other.")
    ]),
UpperBound(id = "!0mwDzZ", fr = dist_clique, to = clique_cover_num, notes = [
    Note(id = "!bYybsT", url = None, text = "We cover the $k$ vertices of the modulator by cliques of size $1$ and cover the remaining clique by another one.")
    ]),
UpperBound(id = "!JtMcJB", fr = clique_cover_num, to = max_independent_set, notes = [
    Note(id = "!h8nG9p", url = None, text = "Every clique of the clique cover partition may contain at most one vertex of the independent set.")
    ]),
UpperBound(id = "!Fxp100", fr = max_independent_set, to = domination_num, notes = [
    Note(id = "!gGtTUf", url = None, text = "Every maximal independent set is also a dominating set because any undominated vertex could be added to the independent set.")
    ]),
UpperBound(id = "!UcXeli", fr = domination_num, to = diameter, notes = [
    Note(id = "!J0jyXi", url = None, text = "An unbounded diameter implies a long path where no vertices that are more than $3$ apart may be dominated by the same dominating vertex, otherwise we could shorten the path. Hence, the number of dominating vertices is also unbounded.")
    ]),
UpperBound(id = "!ogyvLp", fr = dist_bipartite, to = dist_perfect, notes = [
    Note(id = "!UQLQ2Q", url = None, text = "By graph inclusion of the remaining graph classes.")
    ]),
UpperBound(id = "!kXNdFI", fr = dist_bipartite, to = chromatic_num, notes = [
    Note(id = "!xrVJqb", url = None, text = "Removed vertices get one color each and we need only $2$ colors for the rest.")
    ]),
UpperBound(id = "!YHgf7M", fr = average_degree, to = min_degree, notes = [
    Note(id = "!DQzjIV", url = None, text = "By definition. One parameter is special case of the other.")
    ]),
UpperBound(id = "!1LfCs5", fr = book_thickness, to = acn, notes = []),
UpperBound(id = "!pEHP0K", fr = dist_planar, to = acn, notes = []),
UpperBound(id = "!hTp0QP", fr = diameter, to = average_distance, notes = [
    Note(id = "!DQzjIV", url = None, text = "By definition. One parameter is special case of the other.")
    ]),
UpperBound(id = "!x9pao2", fr = average_distance, to = girth, notes = []),
UpperBound(id = "!v4djMN", fr = max_leaf_num, to = fes, notes = []),
UpperBound(id = "!gQqUuq", fr = max_induced_matching, to = diameter, notes = []),
UpperBound(id = "!uzK8uZ", fr = max_independent_set, to = max_induced_matching, notes = []),
UpperBound(id = "!ySKjme", fr = max_matching, to = max_induced_matching, notes = [
    Note(id = "!DQzjIV", url = None, text = "By definition. One parameter is special case of the other.")
    ]),
UpperBound(id = "!cYFhiJ", fr = branch_width, to = treewidth, notes = []),
UpperBound(id = "!J94Xp2", fr = treewidth, to = branch_width, notes = []),
UpperBound(id = "!paKd9Z", fr = rank_width, to = cliquewidth, notes = [
    Note(id = "!wrBAYk", url = "https://www.sciencedirect.com/science/article/pii/S0095895605001528", text = "Proposition 6.3")
    ]),
UpperBound(id = "!zwiV6A", fr = cliquewidth, to = rank_width, notes = [
    Note(id = "!wrBAYk", url = "https://www.sciencedirect.com/science/article/pii/S0095895605001528", text = "Proposition 6.3")
    ]),
UpperBound(id = "!eg3i0f", fr = max_matching, to = vc, notes = [
    Note(id = "!gBA7dc", url = "https://en.wikipedia.org/wiki/K%C5%91nig%27s_theorem_(graph_theory)", text = "Kőnig's theorem")
    ]),
UpperBound(id = "!ZXIraS", fr = vc, to = max_matching, notes = [
    Note(id = "!gBA7dc", url = "https://en.wikipedia.org/wiki/K%C5%91nig%27s_theorem_(graph_theory)", text = "Kőnig's theorem")
    ]),
UpperBound(id = "!haGgbI", fr = edge_connectivity, to = vertex_connectivity, notes = [
    Note(id = "!aQyAEM", url = None, text = "by a simple observation")
    ]),
UpperBound(id = "!tSmPSE", fr = vc, to = neighborhood_diversity, notes = [
    Note(id = "!YgTRtT", url = "https://link.springer.com/article/10.1007/s00453-011-9554-x", text = "Construct $k$ singleton sets, one for each vertex in the vertex cover and at most $2^k$ additional sets, one for each subset of vertices of the vertex cover. ...")
    ]),
UpperBound(id = "!WxT333", fr = neighborhood_diversity, to = shrub_depth, notes = []),
UpperBound(id = "!1r3KyM", fr = twin_cover_num, to = shrub_depth, notes = []),
UpperBound(id = "!2f2OYD", fr = twin_cover_num, to = dist_cluster, notes = [
    Note(id = "!DQzjIV", url = None, text = "By definition. One parameter is special case of the other.")
    ]),
UpperBound(id = "!7rSPl5", fr = vc, to = twin_cover_num, notes = [
    Note(id = "!UQLQ2Q", url = None, text = "By graph inclusion of the remaining graph classes.")
    ]),
UpperBound(id = "!rJOrPy", fr = dist_clique, to = neighborhood_diversity, notes = [
    Note(id = "!YgTRtT", url = "https://link.springer.com/article/10.1007/s00453-011-9554-x", text = "Construct $k$ singleton sets, one for each vertex in the vertex cover and at most $2^k$ additional sets, one for each subset of vertices of the vertex cover. ...")
    ]),
UpperBound(id = "!oWACte", fr = treedepth, to = shrub_depth, notes = []),
UpperBound(id = "!knb7xY", fr = shrub_depth, to = cliquewidth, notes = [])
]

def export():
    return (entries, connections)
