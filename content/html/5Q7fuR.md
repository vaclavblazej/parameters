---
title: "treewidth"
---# treewidth

abbr: tw

tags: [tree decomposition]({{< base >}}html/bzffn0)

functionally equivalent to: [branch width]({{< base >}}html/lIcmuR), [strong inf-coloring number]({{< base >}}html/JQTHZS), [mm-width]({{< base >}}html/d7vRYU)

providers: [ISGCI](https://www.graphclasses.org/classes/par_10.html), [PACE](https://pacechallenge.org/2017/), [PACE](https://pacechallenge.org/2016/)

**Definition:** see [Graph minors. II. Algorithmic aspects of tree-width by Robertson, Seymour]({{< base >}}html/i56ihO)

**Treewidth** is arguably the most important graph parameter.
Intuitively, it describes how close a graph is to a tree.

On this page we cover only an overview of treewidth.
For a more comprehensive introduction, we direct the reader to [Parameterized Algorithms by Cygan, Fomin, Kowalik, Lokshtanov, Marx, Pilipczuk, Pilipczuk, Saurabh]({{< base >}}html/Xlsyce).

## Definition

A *tree decomposition* is a tree $T$ together with a function $\chi$.
To distinguish $T$ from $G$ we call $V(G)$ *vertices* and $V(T)$ *nodes*.
The function $\chi$ maps each node to a set of vertices in $G$.
For each node, the set of vertices assigned to it are called a *bag*.
The tree decomposition $(T,\chi)$ has to follow two rules:

1. Each vertex of the graph is in bags that form a (nonempty) connected subtree of $T$.
2. Each edge of the graph has both of its endpoints in some common bag.

A graph has treewidth $k$ if there exists a tree decomposition such that each bag has size at most $k+1$.

## Dynamic programming

Structure of the decomposition implies several important properties.
The main property is that each bag constitutes a separator.
This allows us to design a bottom-up dynamic programming (DP) algorithms over the tree decomposition for many problems.
For the DP examples below we assume the reader is comfortable in designing DP bottom-up algorithms on trees for problems like vertex cover, dominating set, weighted independent set, etc.

Though it is possible to design DP over tree decomposition directly we usually simplify the decomposition so that at every step only one simple 'thing' is happening.
*Nice tree decomposition* can be computed from a tree decomposition in $O(n)$ time and has the following additional properties:

1. Every node has one of types -- leaf, introduce vertex, forget vertex, join.
2. The decomposition is rooted in some leaf node.
3. Leaf nodes are empty and childess, except the root which has one child.
4. Introduce vertex node has the same bag as its only child, and adds a new vertex.
5. Forget vertex node has the same bag as its only child, and removes one of the vertices.
6. Join node has exactly the same bag as its two children.

If introduce edge nodes are not present, then an edge is introduced when its second incident vertex is introduced.

### Basic DP example

... work in progress

### A few brief examples

* vertex cover -- state: part of the solution in the bag; value: size of the solution in the subgraph; introduce vertex node tries both options and verifies all present edges are present; forget vertex node does nothing interesting; join node sums the solution minus size of the solution in the bag which was counted twice
* ... work in progress

---



<p><div id="../local_5Q7fuR.dot" class="svg-diagram zoomable"></div></p><script type="module">import { initializeSvgToolbelt } from '/parameters/svg-toolbelt.esm.js';Viz.instance().then(function(viz) {fetch('../local_5Q7fuR.dot').then(response => response.text()).then((data) => {var svg = viz.renderSVGElement(data);document.getElementById("../local_5Q7fuR.dot").appendChild(svg);initializeSvgToolbelt('.zoomable', {zoomStep: 0.3,minScale: 1,maxScale: 5,});})});</script>

<p><div id="../graph_property_inclusions_5Q7fuR.dot" class="svg-diagram zoomable"></div></p><script type="module">import { initializeSvgToolbelt } from '/parameters/svg-toolbelt.esm.js';Viz.instance().then(function(viz) {fetch('../graph_property_inclusions_5Q7fuR.dot').then(response => response.text()).then((data) => {var svg = viz.renderSVGElement(data);document.getElementById("../graph_property_inclusions_5Q7fuR.dot").appendChild(svg);initializeSvgToolbelt('.zoomable', {zoomStep: 0.3,minScale: 1,maxScale: 5,});})});</script>

<p><div id="../parameter_inclusions_5Q7fuR.dot" class="svg-diagram zoomable"></div></p><script type="module">import { initializeSvgToolbelt } from '/parameters/svg-toolbelt.esm.js';Viz.instance().then(function(viz) {fetch('../parameter_inclusions_5Q7fuR.dot').then(response => response.text()).then((data) => {var svg = viz.renderSVGElement(data);document.getElementById("../parameter_inclusions_5Q7fuR.dot").appendChild(svg);initializeSvgToolbelt('.zoomable', {zoomStep: 0.3,minScale: 1,maxScale: 5,});})});</script>

---

## Relations

| Other |  | Relation from | Relation to |
| --- | --- | --- | --- |
| [acyclic chromatic number]({{< base >}}html/QGZuUW) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [admissibility]({{< base >}}html/v4sLfO) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [arboricity]({{< base >}}html/zgMenA) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [average degree]({{< base >}}html/z0y4TW) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [average distance]({{< base >}}html/zH8PpT) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [bandwidth]({{< base >}}html/aP5a38) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [bipartite]({{< base >}}html/cLHJkW) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | unbounded | exclusion |
| [bipartite number]({{< base >}}html/1dQQ87) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [bisection bandwidth]({{< base >}}html/wUdmUb) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [block]({{< base >}}html/QrxQsH) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | unbounded | exclusion |
| [book thickness]({{< base >}}html/doijTS) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [boolean width]({{< base >}}html/A2jPWT) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [bounded components]({{< base >}}html/t7c4mp) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [bounded expansion]({{< base >}}html/lFz6Ci) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [boxicity]({{< base >}}html/a7MpiT) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [branch width]({{< base >}}html/lIcmuR) | <span style="display:none">yellow</span><span style="color:#ffd700">■</span> | upper bound | upper bound |
| [c-closure]({{< base >}}html/ou9VU1) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [carving-width]({{< base >}}html/dS6OgO) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [chi-bounded]({{< base >}}html/Jb1we5) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [chordal]({{< base >}}html/Cv1PaJ) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | unbounded | exclusion |
| [chordality]({{< base >}}html/fTqo40) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [chromatic number]({{< base >}}html/w7MmyW) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [clique cover number]({{< base >}}html/VomShB) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [clique-tree-width]({{< base >}}html/7P9WUz) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [clique-width]({{< base >}}html/wg5HuV) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [cluster]({{< base >}}html/WAU7vf) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | unbounded | exclusion |
| [co-cluster]({{< base >}}html/7HR4uV) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | unbounded | exclusion |
| [cograph]({{< base >}}html/9Qd0Mx) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | unbounded | exclusion |
| [complete]({{< base >}}html/EhdXNA) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | unbounded | exclusion |
| [connected]({{< base >}}html/KlMP0i) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | avoids |
| [contraction complexity]({{< base >}}html/LlWzhg) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [cutwidth]({{< base >}}html/TLx1pz) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [cycle]({{< base >}}html/Ti0asF) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [cycles]({{< base >}}html/2iJr52) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [d-admissibility]({{< base >}}html/Pqiy2C) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [d-path-free]({{< base >}}html/s4EiWI) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [degeneracy]({{< base >}}html/VowkuW) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [degree treewidth]({{< base >}}html/nCWUh3) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [diameter]({{< base >}}html/p4bTjp) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [diameter+max degree]({{< base >}}html/ri9Seh) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [distance to bipartite]({{< base >}}html/1yW82F) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [distance to block]({{< base >}}html/xNJnFb) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [distance to bounded components]({{< base >}}html/RPTCxd) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [distance to chordal]({{< base >}}html/OdZQna) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [distance to cluster]({{< base >}}html/aXw3Co) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [distance to co-cluster]({{< base >}}html/hbfWwE) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [distance to cograph]({{< base >}}html/uDXX2i) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [distance to complete]({{< base >}}html/2LDMQ6) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [distance to edgeless]({{< base >}}html/4INs10) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [distance to forest]({{< base >}}html/hQZlLU) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [distance to interval]({{< base >}}html/AVc2K6) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [distance to linear forest]({{< base >}}html/yk7XP0) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [distance to maximum degree]({{< base >}}html/kRR8zx) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [distance to outerplanar]({{< base >}}html/lPHVWU) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [distance to perfect]({{< base >}}html/kJZKgd) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [distance to planar]({{< base >}}html/MLJMRH) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [distance to stars]({{< base >}}html/Z10jME) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [domatic number]({{< base >}}html/KRV6tI) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [domination number]({{< base >}}html/Gq0onN) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [domino treewidth]({{< base >}}html/aEs5ap) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [edge clique cover number]({{< base >}}html/nYQDv6) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [edge connectivity]({{< base >}}html/JbqZoT) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [edge-cut width]({{< base >}}html/ZNqIlN) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [edge-treewidth]({{< base >}}html/pKi2tL) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [edgeless]({{< base >}}html/LsiBbX) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | avoids |
| [excluded minor]({{< base >}}html/5xOuoQ) | <span style="display:none">magenta</span><span style="color:#ee82ee">■</span> | exclusion | unknown to HOPS |
| [excluded planar minor]({{< base >}}html/Gt22Ik) | <span style="display:none">lime</span><span style="color:#00ff00">■</span> | upper bound | unknown to HOPS |
| [excluded top-minor]({{< base >}}html/yOZQM5) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [feedback edge set]({{< base >}}html/HTk9PZ) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [feedback vertex set]({{< base >}}html/GNOiyB) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [flip-width]({{< base >}}html/jYG7BR) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [forest]({{< base >}}html/JngPPm) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [genus]({{< base >}}html/gbaHdw) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [grid]({{< base >}}html/lfYXuK) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | unbounded | exclusion |
| [h-index]({{< base >}}html/GNTwUS) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [interval]({{< base >}}html/p5skoj) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | unbounded | exclusion |
| [iterated type partitions]({{< base >}}html/G1Cwmc) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [linear clique-width]({{< base >}}html/fQj3wU) | <span style="display:none">magenta</span><span style="color:#ee82ee">■</span> | exclusion | unknown to HOPS |
| [linear forest]({{< base >}}html/skQuFN) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [linear NLC-width]({{< base >}}html/v09DMY) | <span style="display:none">magenta</span><span style="color:#ee82ee">■</span> | exclusion | unknown to HOPS |
| [linear rank-width]({{< base >}}html/cHugsk) | <span style="display:none">magenta</span><span style="color:#ee82ee">■</span> | exclusion | unknown to HOPS |
| [maximum clique]({{< base >}}html/q7zHeT) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [maximum degree]({{< base >}}html/UyQ5yM) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [maximum independent set]({{< base >}}html/mHtXUU) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [maximum induced matching]({{< base >}}html/GzMYlT) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [maximum leaf number]({{< base >}}html/BN92vX) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [maximum matching]({{< base >}}html/veU7Jf) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [maximum matching on bipartite graphs]({{< base >}}html/8Mm5qJ) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [merge-width]({{< base >}}html/UWmTKl) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [mim-width]({{< base >}}html/WmIFB1) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [minimum degree]({{< base >}}html/GPmOeT) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [mm-width]({{< base >}}html/d7vRYU) | <span style="display:none">yellow</span><span style="color:#ffd700">■</span> | upper bound | upper bound |
| [modular-width]({{< base >}}html/4bj71L) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [module-width]({{< base >}}html/EV3FqL) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [monadically dependent]({{< base >}}html/dN1D3C) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [monadically stable]({{< base >}}html/jHXy6Y) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [neighborhood diversity]({{< base >}}html/vMs3RS) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [NLC-width]({{< base >}}html/Xrpbv7) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [NLCT-width]({{< base >}}html/mOri44) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [nowhere dense]({{< base >}}html/DhGqJM) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [odd cycle transversal]({{< base >}}html/Ve5ruW) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [outerplanar]({{< base >}}html/0oCyaG) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [overlap treewidth]({{< base >}}html/P8yP3M) | <span style="display:none">lime</span><span style="color:#00ff00">■</span> | upper bound | unknown to HOPS |
| [path]({{< base >}}html/ryPlqz) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [pathwidth]({{< base >}}html/VHClqR) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [pathwidth+maxdegree]({{< base >}}html/6BWcgd) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [perfect]({{< base >}}html/RmssrZ) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | unbounded | exclusion |
| [planar]({{< base >}}html/loZ5LD) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | unbounded | exclusion |
| [radius-inf flip-width]({{< base >}}html/nYXiuT) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [radius-r flip-width]({{< base >}}html/4DIiH0) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [rank-width]({{< base >}}html/fojquT) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [series-parallel]({{< base >}}html/eW1Gic) | <span style="display:none">gray</span><span style="color:#bebebe">■</span> | unknown to HOPS | unknown to HOPS |
| [shrub-depth]({{< base >}}html/NTgNzT) | <span style="display:none">magenta</span><span style="color:#ee82ee">■</span> | exclusion | unknown to HOPS |
| [sim-width]({{< base >}}html/aEGv5N) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [size]({{< base >}}html/F1NpDy) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [slim tree-cut width]({{< base >}}html/oFvl4c) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [sparse twin-width]({{< base >}}html/2FM8hj) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [star]({{< base >}}html/CortlU) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [stars]({{< base >}}html/10JR3F) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [strong coloring number]({{< base >}}html/PxVh3F) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [strong d-coloring number]({{< base >}}html/yihnem) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [strong inf-coloring number]({{< base >}}html/JQTHZS) | <span style="display:none">yellow</span><span style="color:#ffd700">■</span> | upper bound | upper bound |
| [topological bandwidth]({{< base >}}html/SnA7Eq) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [tree]({{< base >}}html/rJyICu) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [tree-cut width]({{< base >}}html/8CgU0P) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [tree-independence number]({{< base >}}html/fNR6QK) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [tree-partition-width]({{< base >}}html/QP01gs) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [treebandwidth]({{< base >}}html/w3LxG1) | <span style="display:none">lime</span><span style="color:#00ff00">■</span> | upper bound | unknown to HOPS |
| [treedepth]({{< base >}}html/KEP2qM) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [treelength]({{< base >}}html/JA2nKw) | <span style="display:none">magenta</span><span style="color:#ee82ee">■</span> | exclusion | unknown to HOPS |
| [treespan]({{< base >}}html/IbKkUQ) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [treewidth]({{< base >}}html/5Q7fuR) | <span style="display:none">yellow</span><span style="color:#ffd700">■</span> | equal | equal |
| [twin-cover number]({{< base >}}html/MUnHA0) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [twin-width]({{< base >}}html/OrH7et) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [vertex connectivity]({{< base >}}html/OyLUe4) | <span style="display:none">gray</span><span style="color:#bebebe">■</span> | unknown to HOPS | unknown to HOPS |
| [vertex cover]({{< base >}}html/4lp9Yj) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [vertex integrity]({{< base >}}html/KVhJFB) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [weak coloring number]({{< base >}}html/KD6n2n) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [weak d-coloring number]({{< base >}}html/3F3oc3) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [weak inf-coloring number]({{< base >}}html/DfwI9E) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [weakly sparse]({{< base >}}html/Qme7wD) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [weakly sparse and merge width]({{< base >}}html/HJjpOL) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |

---

## Results

* 2025 [On a tree-based variant of bandwidth and forbidding simple topological minors by Jacob, Lochet, Paul]({{< base >}}html/EImlRb)
    * page 38 : [treebandwidth]({{< base >}}html/w3LxG1) upper bounds [treewidth]({{< base >}}html/5Q7fuR) by a computable function -- [implied through obstructions]
* 2015 [Parameterized Algorithms by Cygan, Fomin, Kowalik, Lokshtanov, Marx, Pilipczuk, Pilipczuk, Saurabh]({{< base >}}html/Xlsyce)
    * [treewidth]({{< base >}}html/5Q7fuR) -- Very roughly, treewidth captures how similar a graph is to a tree. There are many ways to define ``tree-likeness'' of a graph; ... it appears that the approach most useful from algorithmic and graph theoretical perspectives, is to view tree-likeness of a graph $G$ as the existence of a structural decomposition of $G$ into pieces of bounded size that are connected in a tree-like fashion. This intuitive concept is formalized via the notions of a *tree decomposition* and the *treewidth* of a graph; the latter is a quantitative measure of how good a tree decomposition we can possibly obtain.
* 2012 [Twin-Cover: Beyond Vertex Cover in Parameterized Algorithmics by Ganian]({{< base >}}html/7UoBR6)
    * page 263 : graph classes with bounded [twin-cover number]({{< base >}}html/MUnHA0) are not bounded [treewidth]({{< base >}}html/5Q7fuR) -- There exists graphs with arbitrarily large twin-cover and bounded tree-width and vice-versa.
    * page 263 : graph classes with bounded [treewidth]({{< base >}}html/5Q7fuR) are not bounded [twin-cover number]({{< base >}}html/MUnHA0) -- There exists graphs with arbitrarily large twin-cover and bounded tree-width and vice-versa.
* 2012 [New Width Parameters of Graphs by Vatshelle]({{< base >}}html/nRO7AG)
    * page 40 : [treewidth]({{< base >}}html/5Q7fuR) upper bounds [mm-width]({{< base >}}html/d7vRYU) by a linear function -- Theorem 4.2.5. Let $G$ be a graph, then $\frac 13 (tw(G)+1) \le mmw(G) \le \max(brw(G),1) \le tw(G)+1$
    * page 40 : [mm-width]({{< base >}}html/d7vRYU) upper bounds [treewidth]({{< base >}}html/5Q7fuR) by a linear function -- Theorem 4.2.5. Let $G$ be a graph, then $\frac 13 (tw(G)+1) \le mmw(G) \le \max(brw(G),1) \le tw(G)+1$
* 2010 [Comparing 17 graph parameters by Sasák]({{< base >}}html/XlBXyo)
    * page 17 : graph class [complete]({{< base >}}html/EhdXNA) is not constant [treewidth]({{< base >}}html/5Q7fuR) -- Theorem 2.2
    * page 17 : graph class [grid]({{< base >}}html/lfYXuK) is not constant [treewidth]({{< base >}}html/5Q7fuR) -- Theorem 2.4
    * page 49 : [carving-width]({{< base >}}html/dS6OgO) upper bounds [treewidth]({{< base >}}html/5Q7fuR) by a linear function -- Theorem 5.5 (tw $\prec$ carw) Tree-width is bounded by carving-width.
* 2009 [On tree-partition-width by Wood]({{< base >}}html/p00uyg)
    * page 2 : [tree-partition-width]({{< base >}}html/QP01gs) upper bounds [treewidth]({{< base >}}html/5Q7fuR) by a linear function -- $2twp(G) \ge tw(G)+1$
* 2008 [Simulating Quantum Computation by Contracting Tensor Networks by Markov, Shi]({{< base >}}html/9JAQC7)
    * page 11 : [contraction complexity]({{< base >}}html/LlWzhg) upper bounds [treewidth]({{< base >}}html/5Q7fuR) by a linear function -- Proposition 4.2. ... $cc(G)=tw(G^*)$ ... Lemma 4.4. $(tw(G) - 1)/2 \le tw(G^*) \le \Delta(G)(tw(G) + 1) - 1.$
* 2007 [Graph Treewidth and Geometric Thickness Parameters by Dujmovic, Wood]({{< base >}}html/2q7m9E)
    * page 5 : [treewidth]({{< base >}}html/5Q7fuR) upper bounds [arboricity]({{< base >}}html/zgMenA) by a constant -- Proposition 2. The maximum arboricity of a graph in $\mathcal T_k$ (ed: $k$-tree) is $k$; ...
    * page 8 : [treewidth]({{< base >}}html/5Q7fuR) upper bounds [book thickness]({{< base >}}html/doijTS) by a computable function -- The maximum book thickness ... of a graph $\mathcal T_k$ (ed: $k$-tree) satisfy ... $=k$ for $k \le 2$, $=k+1$ for $k \ge 3$.
* 2005 [On the relationship between NLC-width and linear NLC-width by Gurski, Wanke]({{< base >}}html/FLSQsw)
    * page 8 : [treewidth]({{< base >}}html/5Q7fuR) upper bounds [NLCT-width]({{< base >}}html/mOri44) by a computable function -- The results of [23] imply that each graph class of bounded path-width has bounded linear NLC-width and that each graph class of bounded tree-width has bounded NLCT-width.
* 2000 [Upper bounds to the clique width of graphs by Courcelle, Olariu]({{< base >}}html/ZQrXS8)
    * page 18 : [treewidth]({{< base >}}html/5Q7fuR) upper bounds [clique-width]({{< base >}}html/wg5HuV) by an exponential function -- We will prove that for every undirected graph $G$, $cwd(G) \le 2^{twd(G)+1}+1$ ...
* 1998 [A partial $k$-arboretum of graphs with bounded treewidth by Bodlaender]({{< base >}}html/BOFCWg)
    * page 4 : [pathwidth]({{< base >}}html/VHClqR) upper bounds [treewidth]({{< base >}}html/5Q7fuR) by a linear function -- Lemma 3. (a) For all graphs $G$, $pathwidth(G) \ge treewidth(G)$. ...
    * page 34 : [outerplanar]({{< base >}}html/0oCyaG) upper bounds [treewidth]({{< base >}}html/5Q7fuR) by a constant -- Lemma 78. Every outerplanar graph $G=(V,E)$ has treewidth at most 2.
    * page 37 : graph class [grid]({{< base >}}html/lfYXuK) is not constant [treewidth]({{< base >}}html/5Q7fuR) -- Lemma 88. The treewidth of an $n \times n$ grid graph ... is at least $n$.
    * page 38 : [treewidth]({{< base >}}html/5Q7fuR) upper bounds [minimum degree]({{< base >}}html/GPmOeT) by a constant -- Lemma 90 (Scheffler [94]). Every graph of treewidth at most $k$ contains a vertex of degree at most $k$.
* 1994 [k-NLC graphs and polynomial algorithms by Wanke]({{< base >}}html/SQjcYg)
    * page 6 : [treewidth]({{< base >}}html/5Q7fuR) upper bounds [NLC-width]({{< base >}}html/Xrpbv7) by an exponential function -- Theorem 2.5. For each partial $k$-tree $G$ there is a $(2^{k+1}-1)$-NLC tree $J$ with $G=unlab(J)$.
* 1993 [The Pathwidth and Treewidth of Cographs by Bodlaender, Möhring]({{< base >}}html/a3yKzk)
    * page 4 : graph class [complete]({{< base >}}html/EhdXNA) is not constant [treewidth]({{< base >}}html/5Q7fuR) -- Lemma 3.1 ("clique containment lemma"). Let $(\{X_i\mid u\in I\},T=(I,F))$ be a tree-decomposition of $G=(V,E)$ and let $W \subseteq V$ be a clique in $G$. Then there exists $i \in I$ with $W \subseteq X_i$.
    * page 4 : graph class [bipartite]({{< base >}}html/cLHJkW) is not constant [treewidth]({{< base >}}html/5Q7fuR) -- Lemma 3.2 ("complete bipartite subgraph containment lemma").
* 1993 [On the chordality of a graph by McKee, Scheinerman]({{< base >}}html/IFY0Rw)
    * page 5 : [treewidth]({{< base >}}html/5Q7fuR) upper bounds [chordality]({{< base >}}html/fTqo40) by a constant -- Theorem 7. For any graph $G$, $\mathrm{Chord}(G) \le \tau(G)$.
* 1991 [Graph minors. X. Obstructions to tree-decomposition by Robertson, Seymour]({{< base >}}html/1hPzXs)
    * page 16 : [treewidth]({{< base >}}html/5Q7fuR) upper bounds [branch width]({{< base >}}html/lIcmuR) by a linear function -- (5.1) For any hypergraph $G$, $\max(\beta(G), \gamma(G)) \le \omega(G) + 1 \le \max(\lfloor(3/2)\beta(G)\rfloor, \gamma(G), 1)$.
    * page 16 : [branch width]({{< base >}}html/lIcmuR) upper bounds [treewidth]({{< base >}}html/5Q7fuR) by a linear function -- (5.1) For any hypergraph $G$, $\max(\beta(G), \gamma(G)) \le \omega(G) + 1 \le \max(\lfloor(3/2)\beta(G)\rfloor, \gamma(G), 1)$.
* 1986 [Graph minors. V. Excluding a planar graph by Robertson, Seymour]({{< base >}}html/A82svt)
    * page 2 : [excluded planar minor]({{< base >}}html/Gt22Ik) upper bounds [treewidth]({{< base >}}html/5Q7fuR) by a constant -- (1.5) For every planar graph $H$, there is a number $w$ such that every planar graph with no minor isomorphic to $H$ has tree-wdtih $\le w$
* 1986 [Graph minors. II. Algorithmic aspects of tree-width by Robertson, Seymour]({{< base >}}html/i56ihO)
    * page 1 : [treewidth]({{< base >}}html/5Q7fuR) -- A \emph{tree-decomposition} of $G$ is a family $(X_i \colon i\in I)$ of subsets of $V(G)$, together with a tree $T$ with $V(T)=I$, with the following properties. (W1) $\bigcup(X_i \colon i \in I)=V(G)$. (W2) Every edge of $G$ has both its ends in some $X_i$ ($i \in I$). (W3) For $i,j,k \in I$, if $j$ lies on the path of $T$ from $i$ to $k$ then $X_i \cap X_k \subseteq X_j$. The \emph{width} of the tree-decomposition is $\max(|X_i|-1 \colon i \in I)$. The tree-width of $G$ is the minimum $w \ge 0$ such that $G$ has a tree-decomposition of width $\le w$.
    * page 1 : [treewidth]({{< base >}}html/5Q7fuR) -- Equivalently, the tree-width of $G$ is the minimum $w \ge 0$ such that $G$ is a subgraph of a ``[chordal]({{< base >}}html/Cv1PaJ)'' graph with all cliques of size at most $w + 1$.
* [assumed]({{< base >}}html/9kg0oo)
    * [degree treewidth]({{< base >}}html/nCWUh3) upper bounds [treewidth]({{< base >}}html/5Q7fuR) by a linear function -- by definition
    * [treewidth]({{< base >}}html/5Q7fuR) is equivalent to [treewidth]({{< base >}}html/5Q7fuR) -- assumed
* [unknown source]({{< base >}}html/myit4D)
    * [strong inf-coloring number]({{< base >}}html/JQTHZS) upper bounds [treewidth]({{< base >}}html/5Q7fuR) by a computable function
    * [treewidth]({{< base >}}html/5Q7fuR) upper bounds [strong inf-coloring number]({{< base >}}html/JQTHZS) by a computable function
    * [treewidth]({{< base >}}html/5Q7fuR) upper bounds [excluded top-minor]({{< base >}}html/yOZQM5) by a constant
    * [distance to outerplanar]({{< base >}}html/lPHVWU) upper bounds [treewidth]({{< base >}}html/5Q7fuR) by a linear function -- After removal of $k$ vertices the remaining class has a bounded width $w$. So by including the removed vertices in every bag, we can achieve decomposition of width $w+k$
    * [treewidth]({{< base >}}html/5Q7fuR) upper bounds [book thickness]({{< base >}}html/doijTS) by a computable function
    * [treewidth]({{< base >}}html/5Q7fuR) upper bounds [boolean width]({{< base >}}html/A2jPWT) by a linear function
    * [treewidth]({{< base >}}html/5Q7fuR) upper bounds [tree-independence number]({{< base >}}html/fNR6QK) by a computable function
    * [overlap treewidth]({{< base >}}html/P8yP3M) upper bounds [treewidth]({{< base >}}html/5Q7fuR) by a computable function
    * [treewidth]({{< base >}}html/5Q7fuR) upper bounds [sparse twin-width]({{< base >}}html/2FM8hj) by a tower function