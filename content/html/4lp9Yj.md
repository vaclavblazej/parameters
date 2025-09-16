---
title: "vertex cover"
---# vertex cover

abbr: vc

tags: [vertex removal]({{< base >}}html/e26LM8)

functionally equivalent to: [maximum matching]({{< base >}}html/veU7Jf), [distance to edgeless]({{< base >}}html/4INs10)

providers: [ISGCI](https://www.graphclasses.org/classes/par_2.html), [PACE](https://pacechallenge.org/2019/)

**Definition:** The minimum number of vertices that have to be removed to get an independent set.

**Vertex cover** is perhaps the simplest but useful parameter.
Although the graph class of bounded vertex cover is small, it is often the first parameter for which we aim to design an FPT algorithm.
Vertex cover can be easily 2-approximated in polynomial time.

From the definition, we see the graph of vertex cover $k$ can be partitioned into a *modulator* of size $k$ and an independent set.
The edges here can be only between the vertices of the moduator or from the modulator to the independent set.

FPT algorithms often exploit the fact that vertices of the independent set can be partitioned into $2^k$ groups based on their neighborhood in the modulator.
Now, one can either enumerate all the solutions or notice that whenever a part contains too many vertices we can ignore the vast majority of them as they do not influence the solution.



<p><div id="../local_4lp9Yj.dot" class="svg-diagram zoomable"></div></p><script type="module">import { initializeSvgToolbelt } from 'http://localhost:1313/parameters/svg-toolbelt.esm.js';Viz.instance().then(function(viz) {fetch('../local_4lp9Yj.dot').then(response => response.text()).then((data) => {var svg = viz.renderSVGElement(data);document.getElementById("../local_4lp9Yj.dot").appendChild(svg);initializeSvgToolbelt('.zoomable', {zoomStep: 0.3,minScale: 1,maxScale: 5,});})});</script>

<p><div id="../graph_property_inclusions_4lp9Yj.dot" class="svg-diagram zoomable"></div></p><script type="module">import { initializeSvgToolbelt } from 'http://localhost:1313/parameters/svg-toolbelt.esm.js';Viz.instance().then(function(viz) {fetch('../graph_property_inclusions_4lp9Yj.dot').then(response => response.text()).then((data) => {var svg = viz.renderSVGElement(data);document.getElementById("../graph_property_inclusions_4lp9Yj.dot").appendChild(svg);initializeSvgToolbelt('.zoomable', {zoomStep: 0.3,minScale: 1,maxScale: 5,});})});</script>

<p><div id="../parameter_inclusions_4lp9Yj.dot" class="svg-diagram zoomable"></div></p><script type="module">import { initializeSvgToolbelt } from 'http://localhost:1313/parameters/svg-toolbelt.esm.js';Viz.instance().then(function(viz) {fetch('../parameter_inclusions_4lp9Yj.dot').then(response => response.text()).then((data) => {var svg = viz.renderSVGElement(data);document.getElementById("../parameter_inclusions_4lp9Yj.dot").appendChild(svg);initializeSvgToolbelt('.zoomable', {zoomStep: 0.3,minScale: 1,maxScale: 5,});})});</script>

---

## Relations

| Other |  | Relation from | Relation to |
| --- | --- | --- | --- |
| [acyclic chromatic number]({{< base >}}html/QGZuUW) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [admissibility]({{< base >}}html/v4sLfO) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [arboricity]({{< base >}}html/zgMenA) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [average degree]({{< base >}}html/z0y4TW) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [average distance]({{< base >}}html/zH8PpT) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [bandwidth]({{< base >}}html/aP5a38) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [bipartite]({{< base >}}html/cLHJkW) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | unbounded | exclusion |
| [bipartite number]({{< base >}}html/1dQQ87) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [bisection bandwidth]({{< base >}}html/wUdmUb) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [block]({{< base >}}html/QrxQsH) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | unbounded | exclusion |
| [book thickness]({{< base >}}html/doijTS) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [boolean width]({{< base >}}html/A2jPWT) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [bounded components]({{< base >}}html/t7c4mp) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [bounded expansion]({{< base >}}html/lFz6Ci) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [boxicity]({{< base >}}html/a7MpiT) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [branch width]({{< base >}}html/lIcmuR) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [c-closure]({{< base >}}html/ou9VU1) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [carving-width]({{< base >}}html/dS6OgO) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
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
| [contraction complexity]({{< base >}}html/LlWzhg) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [cutwidth]({{< base >}}html/TLx1pz) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [cycle]({{< base >}}html/Ti0asF) | <span style="display:none">cyan</span><span style="color:#40e0d0">■</span> | unknown to HOPS | exclusion |
| [cycles]({{< base >}}html/2iJr52) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | unbounded | exclusion |
| [d-admissibility]({{< base >}}html/Pqiy2C) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [d-path-free]({{< base >}}html/s4EiWI) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [degeneracy]({{< base >}}html/VowkuW) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [degree treewidth]({{< base >}}html/nCWUh3) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [diameter]({{< base >}}html/p4bTjp) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [diameter+max degree]({{< base >}}html/ri9Seh) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [distance to bipartite]({{< base >}}html/1yW82F) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [distance to block]({{< base >}}html/xNJnFb) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [distance to bounded components]({{< base >}}html/RPTCxd) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [distance to chordal]({{< base >}}html/OdZQna) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [distance to cluster]({{< base >}}html/aXw3Co) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [distance to co-cluster]({{< base >}}html/hbfWwE) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [distance to cograph]({{< base >}}html/uDXX2i) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [distance to complete]({{< base >}}html/2LDMQ6) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [distance to edgeless]({{< base >}}html/4INs10) | <span style="display:none">yellow</span><span style="color:#ffd700">■</span> | equal | equal |
| [distance to forest]({{< base >}}html/hQZlLU) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [distance to interval]({{< base >}}html/AVc2K6) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [distance to linear forest]({{< base >}}html/yk7XP0) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [distance to maximum degree]({{< base >}}html/kRR8zx) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [distance to outerplanar]({{< base >}}html/lPHVWU) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [distance to perfect]({{< base >}}html/kJZKgd) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [distance to planar]({{< base >}}html/MLJMRH) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [distance to stars]({{< base >}}html/Z10jME) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [domatic number]({{< base >}}html/KRV6tI) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [domination number]({{< base >}}html/Gq0onN) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [domino treewidth]({{< base >}}html/aEs5ap) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [edge clique cover number]({{< base >}}html/nYQDv6) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [edge connectivity]({{< base >}}html/JbqZoT) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [edge-cut width]({{< base >}}html/ZNqIlN) | <span style="display:none">magenta</span><span style="color:#ee82ee">■</span> | exclusion | unknown to HOPS |
| [edge-treewidth]({{< base >}}html/pKi2tL) | <span style="display:none">magenta</span><span style="color:#ee82ee">■</span> | exclusion | unknown to HOPS |
| [edgeless]({{< base >}}html/LsiBbX) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | avoids |
| [excluded minor]({{< base >}}html/5xOuoQ) | <span style="display:none">magenta</span><span style="color:#ee82ee">■</span> | exclusion | unknown to HOPS |
| [excluded planar minor]({{< base >}}html/Gt22Ik) | <span style="display:none">gray</span><span style="color:#bebebe">■</span> | unknown to HOPS | unknown to HOPS |
| [excluded top-minor]({{< base >}}html/yOZQM5) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [feedback edge set]({{< base >}}html/HTk9PZ) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [feedback vertex set]({{< base >}}html/GNOiyB) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [flip-width]({{< base >}}html/jYG7BR) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [forest]({{< base >}}html/JngPPm) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | unbounded | exclusion |
| [genus]({{< base >}}html/gbaHdw) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [grid]({{< base >}}html/lfYXuK) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | unbounded | exclusion |
| [h-index]({{< base >}}html/GNTwUS) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [interval]({{< base >}}html/p5skoj) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | unbounded | exclusion |
| [iterated type partitions]({{< base >}}html/G1Cwmc) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [linear clique-width]({{< base >}}html/fQj3wU) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [linear forest]({{< base >}}html/skQuFN) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | unbounded | exclusion |
| [linear NLC-width]({{< base >}}html/v09DMY) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [linear rank-width]({{< base >}}html/cHugsk) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [maximum clique]({{< base >}}html/q7zHeT) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [maximum degree]({{< base >}}html/UyQ5yM) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [maximum independent set]({{< base >}}html/mHtXUU) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [maximum induced matching]({{< base >}}html/GzMYlT) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [maximum leaf number]({{< base >}}html/BN92vX) | <span style="display:none">cyan</span><span style="color:#40e0d0">■</span> | unknown to HOPS | exclusion |
| [maximum matching]({{< base >}}html/veU7Jf) | <span style="display:none">yellow</span><span style="color:#ffd700">■</span> | upper bound | tight bounds |
| [maximum matching on bipartite graphs]({{< base >}}html/8Mm5qJ) | <span style="display:none">green</span><span style="color:#006400">■</span> | tight bounds | exclusion |
| [merge-width]({{< base >}}html/UWmTKl) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [mim-width]({{< base >}}html/WmIFB1) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [minimum degree]({{< base >}}html/GPmOeT) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [mm-width]({{< base >}}html/d7vRYU) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [modular-width]({{< base >}}html/4bj71L) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [module-width]({{< base >}}html/EV3FqL) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [monadically dependent]({{< base >}}html/dN1D3C) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [monadically stable]({{< base >}}html/jHXy6Y) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [neighborhood diversity]({{< base >}}html/vMs3RS) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [NLC-width]({{< base >}}html/Xrpbv7) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [NLCT-width]({{< base >}}html/mOri44) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [nowhere dense]({{< base >}}html/DhGqJM) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [odd cycle transversal]({{< base >}}html/Ve5ruW) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [outerplanar]({{< base >}}html/0oCyaG) | <span style="display:none">cyan</span><span style="color:#40e0d0">■</span> | unknown to HOPS | exclusion |
| [overlap treewidth]({{< base >}}html/P8yP3M) | <span style="display:none">magenta</span><span style="color:#ee82ee">■</span> | exclusion | unknown to HOPS |
| [path]({{< base >}}html/ryPlqz) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | unbounded | exclusion |
| [pathwidth]({{< base >}}html/VHClqR) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [pathwidth+maxdegree]({{< base >}}html/6BWcgd) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [perfect]({{< base >}}html/RmssrZ) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | unbounded | exclusion |
| [planar]({{< base >}}html/loZ5LD) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | unbounded | exclusion |
| [radius-inf flip-width]({{< base >}}html/nYXiuT) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [radius-r flip-width]({{< base >}}html/4DIiH0) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [rank-width]({{< base >}}html/fojquT) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [series-parallel]({{< base >}}html/eW1Gic) | <span style="display:none">gray</span><span style="color:#bebebe">■</span> | unknown to HOPS | unknown to HOPS |
| [shrub-depth]({{< base >}}html/NTgNzT) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [sim-width]({{< base >}}html/aEGv5N) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [size]({{< base >}}html/F1NpDy) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [slim tree-cut width]({{< base >}}html/oFvl4c) | <span style="display:none">magenta</span><span style="color:#ee82ee">■</span> | exclusion | unknown to HOPS |
| [sparse twin-width]({{< base >}}html/2FM8hj) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [star]({{< base >}}html/CortlU) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [stars]({{< base >}}html/10JR3F) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | unbounded | exclusion |
| [strong coloring number]({{< base >}}html/PxVh3F) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [strong d-coloring number]({{< base >}}html/yihnem) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [strong inf-coloring number]({{< base >}}html/JQTHZS) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [topological bandwidth]({{< base >}}html/SnA7Eq) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [tree]({{< base >}}html/rJyICu) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | unbounded | exclusion |
| [tree-cut width]({{< base >}}html/8CgU0P) | <span style="display:none">magenta</span><span style="color:#ee82ee">■</span> | exclusion | unknown to HOPS |
| [tree-independence number]({{< base >}}html/fNR6QK) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [tree-partition-width]({{< base >}}html/QP01gs) | <span style="display:none">magenta</span><span style="color:#ee82ee">■</span> | exclusion | unknown to HOPS |
| [treebandwidth]({{< base >}}html/w3LxG1) | <span style="display:none">magenta</span><span style="color:#ee82ee">■</span> | exclusion | unknown to HOPS |
| [treedepth]({{< base >}}html/KEP2qM) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [treelength]({{< base >}}html/JA2nKw) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [treespan]({{< base >}}html/IbKkUQ) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [treewidth]({{< base >}}html/5Q7fuR) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [twin-cover number]({{< base >}}html/MUnHA0) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [twin-width]({{< base >}}html/OrH7et) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [vertex connectivity]({{< base >}}html/OyLUe4) | <span style="display:none">gray</span><span style="color:#bebebe">■</span> | unknown to HOPS | unknown to HOPS |
| [vertex cover]({{< base >}}html/4lp9Yj) | <span style="display:none">yellow</span><span style="color:#ffd700">■</span> | equal | equal |
| [vertex integrity]({{< base >}}html/KVhJFB) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [weak coloring number]({{< base >}}html/KD6n2n) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [weak d-coloring number]({{< base >}}html/3F3oc3) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [weak inf-coloring number]({{< base >}}html/DfwI9E) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [weakly sparse]({{< base >}}html/Qme7wD) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [weakly sparse and merge width]({{< base >}}html/HJjpOL) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |

---

## Results

* 2025 [On a tree-based variant of bandwidth and forbidding simple topological minors by Jacob, Lochet, Paul]({{< base >}}html/EImlRb)
    * page 36 : [vertex cover]({{< base >}}html/4lp9Yj) upper and lower bounds [maximum matching]({{< base >}}html/veU7Jf) by a linear function -- ... discovered independently by Fanica Gavril and Mihalis Yannakakis. Theorem 50. In a graph $G$, we have $\mu(G) \le {\rm vc}(G) \le 2\mu(G)$, where $\mu(G)$ is the maximum matching number of $G$.
    * page 36 : [maximum matching]({{< base >}}html/veU7Jf) upper bounds [vertex cover]({{< base >}}html/4lp9Yj) by a linear function -- ... discovered independently by Fanica Gavril and Mihalis Yannakakis. Theorem 50. In a graph $G$, we have $\mu(G) \le {\rm vc}(G) \le 2\mu(G)$, where $\mu(G)$ is the maximum matching number of $G$.
* 2022 [Expanding the Graph Parameter Hierarchy by Tran]({{< base >}}html/uXViPE)
    * page 18 : [vertex cover]({{< base >}}html/4lp9Yj) upper bounds [twin-cover number]({{< base >}}html/MUnHA0) by a linear function -- By definition
    * page 18 : graph class [complete]({{< base >}}html/EhdXNA) is not constant [vertex cover]({{< base >}}html/4lp9Yj) -- Note that a clique of size $n$ has ... a vertex cover number of $n-1$
    * page 23 : [vertex cover]({{< base >}}html/4lp9Yj) upper bounds [neighborhood diversity]({{< base >}}html/vMs3RS) by an exponential function -- Proposition 4.3. Vertex Cover Number strictly upper bounds Neighborhood Diversity.
    * page 23 : graph classes with bounded [neighborhood diversity]({{< base >}}html/vMs3RS) are not bounded [vertex cover]({{< base >}}html/4lp9Yj) -- Proposition 4.3. Vertex Cover Number strictly upper bounds Neighborhood Diversity.
    * page 29 : graph classes with bounded [edge clique cover number]({{< base >}}html/nYQDv6) are not bounded [vertex cover]({{< base >}}html/4lp9Yj) -- Proposition 4.13. Edge Clique Cover Number is incomparable to Vertex Cover Number.
    * page 29 : graph classes with bounded [vertex cover]({{< base >}}html/4lp9Yj) are not bounded [edge clique cover number]({{< base >}}html/nYQDv6) -- Proposition 4.13. Edge Clique Cover Number is incomparable to Vertex Cover Number.
    * page 34 : graph classes with bounded [c-closure]({{< base >}}html/ou9VU1) are not bounded [vertex cover]({{< base >}}html/4lp9Yj) -- Proposition 5.3. $c$-Closure is incomparable to Vertex Cover Number.
    * page 34 : graph classes with bounded [vertex cover]({{< base >}}html/4lp9Yj) are not bounded [c-closure]({{< base >}}html/ou9VU1) -- Proposition 5.3. $c$-Closure is incomparable to Vertex Cover Number.
* 2012 [Twin-Cover: Beyond Vertex Cover in Parameterized Algorithmics by Ganian]({{< base >}}html/7UoBR6)
    * page 263 : graph classes with bounded [twin-cover number]({{< base >}}html/MUnHA0) are not bounded [vertex cover]({{< base >}}html/4lp9Yj) -- The vertex cover of graphs of bounded twin-cover may be arbitrarily large.
* [Comparing Graph Parameters by Schröder]({{< base >}}html/DYGiYb)
    * page 15 : graph classes with bounded [vertex cover]({{< base >}}html/4lp9Yj) are not bounded [domination number]({{< base >}}html/Gq0onN) -- Proposition 3.5
    * page 24 : graph classes with bounded [vertex cover]({{< base >}}html/4lp9Yj) are not bounded [genus]({{< base >}}html/gbaHdw) -- Proposition 3.18
    * page 24 : graph classes with bounded [vertex cover]({{< base >}}html/4lp9Yj) are not bounded [maximum degree]({{< base >}}html/UyQ5yM) -- Proposition 3.19
    * page 24 : graph classes with bounded [vertex cover]({{< base >}}html/4lp9Yj) are not bounded [bisection bandwidth]({{< base >}}html/wUdmUb) -- Proposition 3.20
* [unknown source]({{< base >}}html/myit4D)
    * [maximum matching on bipartite graphs]({{< base >}}html/8Mm5qJ) upper and lower bounds [vertex cover]({{< base >}}html/4lp9Yj) by a linear function -- Kőnig's theorem
    * [vertex cover]({{< base >}}html/4lp9Yj) upper bounds [neighborhood diversity]({{< base >}}html/vMs3RS) by an exponential function
    * [vertex cover]({{< base >}}html/4lp9Yj) is equivalent to [distance to edgeless]({{< base >}}html/4INs10)
    * [distance to edgeless]({{< base >}}html/4INs10) is equivalent to [vertex cover]({{< base >}}html/4lp9Yj)
    * [edgeless]({{< base >}}html/LsiBbX) upper bounds [vertex cover]({{< base >}}html/4lp9Yj) by a constant
    * [star]({{< base >}}html/CortlU) upper bounds [vertex cover]({{< base >}}html/4lp9Yj) by a constant -- trivially
* [assumed]({{< base >}}html/9kg0oo)
    * [vertex cover]({{< base >}}html/4lp9Yj) upper bounds [twin-cover number]({{< base >}}html/MUnHA0) by a linear function -- By definition
    * [size]({{< base >}}html/F1NpDy) upper bounds [vertex cover]({{< base >}}html/4lp9Yj) by a linear function -- By definition
    * [vertex cover]({{< base >}}html/4lp9Yj) is equivalent to [vertex cover]({{< base >}}html/4lp9Yj) -- assumed