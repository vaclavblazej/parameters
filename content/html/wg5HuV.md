---
title: "clique-width"
---# clique-width

abbr: cw

functionally equivalent to: [radius-inf flip-width]({{< base >}}html/nYXiuT), [module-width]({{< base >}}html/EV3FqL), [boolean width]({{< base >}}html/A2jPWT), [rank-width]({{< base >}}html/fojquT), [NLC-width]({{< base >}}html/Xrpbv7)

providers: [ISGCI](https://www.graphclasses.org/classes/par_12.html)

**Definition:** Minimum number of labels (colors) required to construct the graph using the following operations for constructing labeled graphs: 1) create a new labeled vertex, 2) disjoint union, 3) complete join between two labels, and 4) change all vertices from one to another label.

**Clique-width** is a generalization of [treewidth]({{< base >}}html/5Q7fuR) to dense graphs.
There are quite a few parameters that are functionally equivalent to cilque-width; notably [rank-width]({{< base >}}html/fojquT) which has a better bound for graphs of bounded treewidth.



<p><div id="../local_wg5HuV.dot" class="svg-diagram zoomable"></div></p><script type="module">import { initializeSvgToolbelt } from 'http://localhost:1313/parameters/svg-toolbelt.esm.js';Viz.instance().then(function(viz) {fetch('../local_wg5HuV.dot').then(response => response.text()).then((data) => {var svg = viz.renderSVGElement(data);document.getElementById("../local_wg5HuV.dot").appendChild(svg);initializeSvgToolbelt('.zoomable', {zoomStep: 0.3,minScale: 1,maxScale: 5,});})});</script>

<p><div id="../graph_property_inclusions_wg5HuV.dot" class="svg-diagram zoomable"></div></p><script type="module">import { initializeSvgToolbelt } from 'http://localhost:1313/parameters/svg-toolbelt.esm.js';Viz.instance().then(function(viz) {fetch('../graph_property_inclusions_wg5HuV.dot').then(response => response.text()).then((data) => {var svg = viz.renderSVGElement(data);document.getElementById("../graph_property_inclusions_wg5HuV.dot").appendChild(svg);initializeSvgToolbelt('.zoomable', {zoomStep: 0.3,minScale: 1,maxScale: 5,});})});</script>

<p><div id="../parameter_inclusions_wg5HuV.dot" class="svg-diagram zoomable"></div></p><script type="module">import { initializeSvgToolbelt } from 'http://localhost:1313/parameters/svg-toolbelt.esm.js';Viz.instance().then(function(viz) {fetch('../parameter_inclusions_wg5HuV.dot').then(response => response.text()).then((data) => {var svg = viz.renderSVGElement(data);document.getElementById("../parameter_inclusions_wg5HuV.dot").appendChild(svg);initializeSvgToolbelt('.zoomable', {zoomStep: 0.3,minScale: 1,maxScale: 5,});})});</script>

---

## Relations

| Other |  | Relation from | Relation to |
| --- | --- | --- | --- |
| [acyclic chromatic number]({{< base >}}html/QGZuUW) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [admissibility]({{< base >}}html/v4sLfO) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [arboricity]({{< base >}}html/zgMenA) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [average degree]({{< base >}}html/z0y4TW) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [average distance]({{< base >}}html/zH8PpT) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [bandwidth]({{< base >}}html/aP5a38) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [bipartite]({{< base >}}html/cLHJkW) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | unbounded | exclusion |
| [bipartite number]({{< base >}}html/1dQQ87) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [bisection bandwidth]({{< base >}}html/wUdmUb) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [block]({{< base >}}html/QrxQsH) | <span style="display:none">cyan</span><span style="color:#40e0d0">■</span> | unknown to HOPS | exclusion |
| [book thickness]({{< base >}}html/doijTS) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [boolean width]({{< base >}}html/A2jPWT) | <span style="display:none">yellow</span><span style="color:#ffd700">■</span> | upper bound | upper bound |
| [bounded components]({{< base >}}html/t7c4mp) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [bounded expansion]({{< base >}}html/lFz6Ci) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | avoids |
| [boxicity]({{< base >}}html/a7MpiT) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [branch width]({{< base >}}html/lIcmuR) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [c-closure]({{< base >}}html/ou9VU1) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [carving-width]({{< base >}}html/dS6OgO) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [chi-bounded]({{< base >}}html/Jb1we5) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [chordal]({{< base >}}html/Cv1PaJ) | <span style="display:none">cyan</span><span style="color:#40e0d0">■</span> | unknown to HOPS | exclusion |
| [chordality]({{< base >}}html/fTqo40) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [chromatic number]({{< base >}}html/w7MmyW) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [clique cover number]({{< base >}}html/VomShB) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [clique-tree-width]({{< base >}}html/7P9WUz) | <span style="display:none">lime</span><span style="color:#00ff00">■</span> | upper bound | unknown to HOPS |
| [clique-width]({{< base >}}html/wg5HuV) | <span style="display:none">yellow</span><span style="color:#ffd700">■</span> | equal | equal |
| [cluster]({{< base >}}html/WAU7vf) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [co-cluster]({{< base >}}html/7HR4uV) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [cograph]({{< base >}}html/9Qd0Mx) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [complete]({{< base >}}html/EhdXNA) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [connected]({{< base >}}html/KlMP0i) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | avoids |
| [contraction complexity]({{< base >}}html/LlWzhg) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [cutwidth]({{< base >}}html/TLx1pz) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [cycle]({{< base >}}html/Ti0asF) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [cycles]({{< base >}}html/2iJr52) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [d-admissibility]({{< base >}}html/Pqiy2C) | <span style="display:none">magenta</span><span style="color:#ee82ee">■</span> | exclusion | unknown to HOPS |
| [d-path-free]({{< base >}}html/s4EiWI) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [degeneracy]({{< base >}}html/VowkuW) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [degree treewidth]({{< base >}}html/nCWUh3) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [diameter]({{< base >}}html/p4bTjp) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [diameter+max degree]({{< base >}}html/ri9Seh) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [distance to bipartite]({{< base >}}html/1yW82F) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [distance to block]({{< base >}}html/xNJnFb) | <span style="display:none">cyan</span><span style="color:#40e0d0">■</span> | unknown to HOPS | exclusion |
| [distance to bounded components]({{< base >}}html/RPTCxd) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [distance to chordal]({{< base >}}html/OdZQna) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [distance to cluster]({{< base >}}html/aXw3Co) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [distance to co-cluster]({{< base >}}html/hbfWwE) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [distance to cograph]({{< base >}}html/uDXX2i) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [distance to complete]({{< base >}}html/2LDMQ6) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [distance to edgeless]({{< base >}}html/4INs10) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [distance to forest]({{< base >}}html/hQZlLU) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [distance to interval]({{< base >}}html/AVc2K6) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [distance to linear forest]({{< base >}}html/yk7XP0) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [distance to maximum degree]({{< base >}}html/kRR8zx) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [distance to outerplanar]({{< base >}}html/lPHVWU) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [distance to perfect]({{< base >}}html/kJZKgd) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [distance to planar]({{< base >}}html/MLJMRH) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [distance to stars]({{< base >}}html/Z10jME) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [domatic number]({{< base >}}html/KRV6tI) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [domination number]({{< base >}}html/Gq0onN) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [domino treewidth]({{< base >}}html/aEs5ap) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [edge clique cover number]({{< base >}}html/nYQDv6) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [edge connectivity]({{< base >}}html/JbqZoT) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [edge-cut width]({{< base >}}html/ZNqIlN) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [edge-treewidth]({{< base >}}html/pKi2tL) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [edgeless]({{< base >}}html/LsiBbX) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | avoids |
| [excluded minor]({{< base >}}html/5xOuoQ) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | avoids |
| [excluded planar minor]({{< base >}}html/Gt22Ik) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | avoids |
| [excluded top-minor]({{< base >}}html/yOZQM5) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | avoids |
| [feedback edge set]({{< base >}}html/HTk9PZ) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [feedback vertex set]({{< base >}}html/GNOiyB) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [flip-width]({{< base >}}html/jYG7BR) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [forest]({{< base >}}html/JngPPm) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [genus]({{< base >}}html/gbaHdw) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [grid]({{< base >}}html/lfYXuK) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | unbounded | exclusion |
| [h-index]({{< base >}}html/GNTwUS) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [interval]({{< base >}}html/p5skoj) | <span style="display:none">cyan</span><span style="color:#40e0d0">■</span> | unknown to HOPS | exclusion |
| [iterated type partitions]({{< base >}}html/G1Cwmc) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [linear clique-width]({{< base >}}html/fQj3wU) | <span style="display:none">lime</span><span style="color:#00ff00">■</span> | upper bound | unknown to HOPS |
| [linear forest]({{< base >}}html/skQuFN) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [linear NLC-width]({{< base >}}html/v09DMY) | <span style="display:none">lime</span><span style="color:#00ff00">■</span> | upper bound | unknown to HOPS |
| [linear rank-width]({{< base >}}html/cHugsk) | <span style="display:none">lime</span><span style="color:#00ff00">■</span> | upper bound | unknown to HOPS |
| [maximum clique]({{< base >}}html/q7zHeT) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [maximum degree]({{< base >}}html/UyQ5yM) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [maximum independent set]({{< base >}}html/mHtXUU) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [maximum induced matching]({{< base >}}html/GzMYlT) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [maximum leaf number]({{< base >}}html/BN92vX) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [maximum matching]({{< base >}}html/veU7Jf) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [maximum matching on bipartite graphs]({{< base >}}html/8Mm5qJ) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [merge-width]({{< base >}}html/UWmTKl) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [mim-width]({{< base >}}html/WmIFB1) | <span style="display:none">orange</span><span style="color:#ff8c00">■</span> | unknown to HOPS | upper bound |
| [minimum degree]({{< base >}}html/GPmOeT) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [mm-width]({{< base >}}html/d7vRYU) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [modular-width]({{< base >}}html/4bj71L) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [module-width]({{< base >}}html/EV3FqL) | <span style="display:none">yellow</span><span style="color:#ffd700">■</span> | upper bound | upper bound |
| [monadically dependent]({{< base >}}html/dN1D3C) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [monadically stable]({{< base >}}html/jHXy6Y) | <span style="display:none">magenta</span><span style="color:#ee82ee">■</span> | exclusion | unknown to HOPS |
| [neighborhood diversity]({{< base >}}html/vMs3RS) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [NLC-width]({{< base >}}html/Xrpbv7) | <span style="display:none">yellow</span><span style="color:#ffd700">■</span> | upper bound | upper bound |
| [NLCT-width]({{< base >}}html/mOri44) | <span style="display:none">lime</span><span style="color:#00ff00">■</span> | upper bound | unknown to HOPS |
| [nowhere dense]({{< base >}}html/DhGqJM) | <span style="display:none">magenta</span><span style="color:#ee82ee">■</span> | exclusion | unknown to HOPS |
| [odd cycle transversal]({{< base >}}html/Ve5ruW) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [outerplanar]({{< base >}}html/0oCyaG) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [overlap treewidth]({{< base >}}html/P8yP3M) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [path]({{< base >}}html/ryPlqz) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [pathwidth]({{< base >}}html/VHClqR) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [pathwidth+maxdegree]({{< base >}}html/6BWcgd) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [perfect]({{< base >}}html/RmssrZ) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | unbounded | exclusion |
| [planar]({{< base >}}html/loZ5LD) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | unbounded | exclusion |
| [radius-inf flip-width]({{< base >}}html/nYXiuT) | <span style="display:none">yellow</span><span style="color:#ffd700">■</span> | upper bound | upper bound |
| [radius-r flip-width]({{< base >}}html/4DIiH0) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [rank-width]({{< base >}}html/fojquT) | <span style="display:none">yellow</span><span style="color:#ffd700">■</span> | tight bounds | upper bound |
| [series-parallel]({{< base >}}html/eW1Gic) | <span style="display:none">gray</span><span style="color:#bebebe">■</span> | unknown to HOPS | unknown to HOPS |
| [shrub-depth]({{< base >}}html/NTgNzT) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [sim-width]({{< base >}}html/aEGv5N) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [size]({{< base >}}html/F1NpDy) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [slim tree-cut width]({{< base >}}html/oFvl4c) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [sparse twin-width]({{< base >}}html/2FM8hj) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [star]({{< base >}}html/CortlU) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [stars]({{< base >}}html/10JR3F) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [strong coloring number]({{< base >}}html/PxVh3F) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [strong d-coloring number]({{< base >}}html/yihnem) | <span style="display:none">magenta</span><span style="color:#ee82ee">■</span> | exclusion | unknown to HOPS |
| [strong inf-coloring number]({{< base >}}html/JQTHZS) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [topological bandwidth]({{< base >}}html/SnA7Eq) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [tree]({{< base >}}html/rJyICu) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [tree-cut width]({{< base >}}html/8CgU0P) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [tree-independence number]({{< base >}}html/fNR6QK) | <span style="display:none">magenta</span><span style="color:#ee82ee">■</span> | exclusion | unknown to HOPS |
| [tree-partition-width]({{< base >}}html/QP01gs) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [treebandwidth]({{< base >}}html/w3LxG1) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [treedepth]({{< base >}}html/KEP2qM) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [treelength]({{< base >}}html/JA2nKw) | <span style="display:none">magenta</span><span style="color:#ee82ee">■</span> | exclusion | unknown to HOPS |
| [treespan]({{< base >}}html/IbKkUQ) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [treewidth]({{< base >}}html/5Q7fuR) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [twin-cover number]({{< base >}}html/MUnHA0) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [twin-width]({{< base >}}html/OrH7et) | <span style="display:none">red</span><span style="color:#ff0000">■</span> | exclusion | upper bound |
| [vertex connectivity]({{< base >}}html/OyLUe4) | <span style="display:none">gray</span><span style="color:#bebebe">■</span> | unknown to HOPS | unknown to HOPS |
| [vertex cover]({{< base >}}html/4lp9Yj) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [vertex integrity]({{< base >}}html/KVhJFB) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [weak coloring number]({{< base >}}html/KD6n2n) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |
| [weak d-coloring number]({{< base >}}html/3F3oc3) | <span style="display:none">magenta</span><span style="color:#ee82ee">■</span> | exclusion | unknown to HOPS |
| [weak inf-coloring number]({{< base >}}html/DfwI9E) | <span style="display:none">green</span><span style="color:#006400">■</span> | upper bound | exclusion |
| [weakly sparse]({{< base >}}html/Qme7wD) | <span style="display:none">magenta</span><span style="color:#ee82ee">■</span> | exclusion | unknown to HOPS |
| [weakly sparse and merge width]({{< base >}}html/HJjpOL) | <span style="display:none">blue</span><span style="color:#0000ff">■</span> | exclusion | exclusion |

---

## Results

* 2022 [Expanding the Graph Parameter Hierarchy by Tran]({{< base >}}html/uXViPE)
    * page 25 : [modular-width]({{< base >}}html/4bj71L) upper bounds [clique-width]({{< base >}}html/wg5HuV) by a computable function -- Proposition 4.6. Modular-width strictly upper bounds Clique-width.
    * page 25 : graph classes with bounded [clique-width]({{< base >}}html/wg5HuV) are not bounded [modular-width]({{< base >}}html/4bj71L) -- Proposition 4.6. Modular-width strictly upper bounds Clique-width.
    * page 36 : [clique-width]({{< base >}}html/wg5HuV) upper bounds [twin-width]({{< base >}}html/OrH7et) by a tower function -- Proposition 6.2. Clique-width strictly upper bounds Twin-width.
    * page 36 : graph classes with bounded [twin-width]({{< base >}}html/OrH7et) are not bounded [clique-width]({{< base >}}html/wg5HuV) -- Proposition 6.2. Clique-width strictly upper bounds Twin-width.
* 2019 [The Graph Parameter Hierarchy by Sorge]({{< base >}}html/VnTIL0)
    * page 9 : [distance to cograph]({{< base >}}html/uDXX2i) upper bounds [clique-width]({{< base >}}html/wg5HuV) by an exponential function -- Lemma 4.17. The distance $c$ to a cograph upper bounds the cliquewidth $q$. We have $q \le 2^{3+c}-1$.
* 2012 [Twin-Cover: Beyond Vertex Cover in Parameterized Algorithmics by Ganian]({{< base >}}html/7UoBR6)
    * page 263 : [twin-cover number]({{< base >}}html/MUnHA0) upper bounds [clique-width]({{< base >}}html/wg5HuV) by a constant -- The clique-width of graphs of twin-cover $k$ is at most $k+2$.
* 2006 [Approximating clique-width and branch-width by Oum, Seymour]({{< base >}}html/1ZTWBd)
    * page 9 : [rank-width]({{< base >}}html/fojquT) upper and lower bounds [clique-width]({{< base >}}html/wg5HuV) by an exponential function -- Proposition 6.3
    * page 9 : [clique-width]({{< base >}}html/wg5HuV) upper bounds [rank-width]({{< base >}}html/fojquT) by a linear function -- Proposition 6.3
* 2005 [On the relationship between NLC-width and linear NLC-width by Gurski, Wanke]({{< base >}}html/FLSQsw)
    * page 8 : [clique-tree-width]({{< base >}}html/7P9WUz) upper bounds [clique-width]({{< base >}}html/wg5HuV) by a linear function
* 2000 [Upper bounds to the clique width of graphs by Courcelle, Olariu]({{< base >}}html/ZQrXS8)
    * page 18 : [treewidth]({{< base >}}html/5Q7fuR) upper bounds [clique-width]({{< base >}}html/wg5HuV) by an exponential function -- We will prove that for every undirected graph $G$, $cwd(G) \le 2^{twd(G)+1}+1$ ...
* 1998 [Clique-decomposition, NLC-decomposition and modular decomposition—relationships and results for random graphs by Johansson]({{< base >}}html/W2nwG4)
    * [clique-width]({{< base >}}html/wg5HuV) upper bounds [NLC-width]({{< base >}}html/Xrpbv7) by a linear function
    * [NLC-width]({{< base >}}html/Xrpbv7) upper bounds [clique-width]({{< base >}}html/wg5HuV) by a linear function
* [Comparing Graph Parameters by Schröder]({{< base >}}html/DYGiYb)
    * page 16 : graph classes with bounded [clique cover number]({{< base >}}html/VomShB) are not bounded [clique-width]({{< base >}}html/wg5HuV) -- Proposition 3.9
    * page 23 : graph classes with bounded [genus]({{< base >}}html/gbaHdw) are not bounded [clique-width]({{< base >}}html/wg5HuV) -- Proposition 3.17
    * page 23 : graph classes with bounded [distance to planar]({{< base >}}html/MLJMRH) are not bounded [clique-width]({{< base >}}html/wg5HuV) -- Proposition 3.17
    * page 28 : graph classes with bounded [maximum degree]({{< base >}}html/UyQ5yM) are not bounded [clique-width]({{< base >}}html/wg5HuV) -- Proposition 3.26
    * page 28 : graph classes with bounded [distance to bipartite]({{< base >}}html/1yW82F) are not bounded [clique-width]({{< base >}}html/wg5HuV) -- Proposition 3.26
    * page 33 : graph classes with bounded [bisection bandwidth]({{< base >}}html/wUdmUb) are not bounded [clique-width]({{< base >}}html/wg5HuV) -- Proposition 3.32
* [assumed]({{< base >}}html/9kg0oo)
    * [clique-width]({{< base >}}html/wg5HuV) is equivalent to [clique-width]({{< base >}}html/wg5HuV) -- assumed
* [unknown source]({{< base >}}html/myit4D)
    * [linear clique-width]({{< base >}}html/fQj3wU) upper bounds [clique-width]({{< base >}}html/wg5HuV) by a linear function
    * [clique-width]({{< base >}}html/wg5HuV) upper bounds [boolean width]({{< base >}}html/A2jPWT) by a linear function
    * [boolean width]({{< base >}}html/A2jPWT) upper bounds [clique-width]({{< base >}}html/wg5HuV) by an exponential function
    * [module-width]({{< base >}}html/EV3FqL) upper bounds [clique-width]({{< base >}}html/wg5HuV) by a computable function
    * [clique-width]({{< base >}}html/wg5HuV) upper bounds [module-width]({{< base >}}html/EV3FqL) by a computable function
    * [modular-width]({{< base >}}html/4bj71L) upper bounds [clique-width]({{< base >}}html/wg5HuV) by a computable function
    * [clique-width]({{< base >}}html/wg5HuV) upper bounds [mim-width]({{< base >}}html/WmIFB1) by a linear function
    * [clique-width]({{< base >}}html/wg5HuV) upper bounds [twin-width]({{< base >}}html/OrH7et) by a tower function
    * [clique-width]({{< base >}}html/wg5HuV) upper bounds [chi-bounded]({{< base >}}html/Jb1we5) by a constant