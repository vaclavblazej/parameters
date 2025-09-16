---
layout: "single"
title: "Hierarchy"
---

# HOPS web view

This page contains lists for:

* [parameters](#parameters)
* [graph classes and properties](#graph-classes-and-properties)
* [sources](#sources)
* [tags](#tags)

---

## Parameters

### Simplified Hasse hierarchy ([source](parameters_simplified.dot))

<p><div id="parameters_simplified.dot" class="svg-diagram zoomable"></div></p><script type="module">import { initializeSvgToolbelt } from '/parameters/svg-toolbelt.esm.js';Viz.instance().then(function(viz) {fetch('parameters_simplified.dot').then(response => response.text()).then((data) => {var svg = viz.renderSVGElement(data);document.getElementById("parameters_simplified.dot").appendChild(svg);initializeSvgToolbelt('.zoomable', {zoomStep: 0.3,minScale: 1,maxScale: 5,});})});</script>



### Hasse hierarchy ([source](parameters.dot))

<p><div id="parameters.dot" class="svg-diagram zoomable"></div></p><script type="module">import { initializeSvgToolbelt } from '/parameters/svg-toolbelt.esm.js';Viz.instance().then(function(viz) {fetch('parameters.dot').then(response => response.text()).then((data) => {var svg = viz.renderSVGElement(data);document.getElementById("parameters.dot").appendChild(svg);initializeSvgToolbelt('.zoomable', {zoomStep: 0.3,minScale: 1,maxScale: 5,});})});</script>



### Simplified comparison table ([pdf](table_simplified.pdf), [full-pdf](table.pdf))


<object data="table_simplified.pdf" type="application/pdf" width="100%" height="480px"><embed src="table_simplified.pdf"><p>This browser does not support PDFs. Please download the PDF to view it: <a href="table_simplified.pdf">Download PDF</a>.</p></embed></object>



---

### All parameters in HOPS

| Parameter | <a href="{{< base >}}docs/legend/#relevance">*</a>Relevance |
| --- | --- |
| [acyclic chromatic number]({{< base >}}html/QGZuUW) | █████░░░░ |
| [admissibility]({{< base >}}html/v4sLfO) | █████░░░░ |
| [arboricity]({{< base >}}html/zgMenA) | █████░░░░ |
| [average degree]({{< base >}}html/z0y4TW) | ██░░░░░░░ |
| [average distance]({{< base >}}html/zH8PpT) | ███░░░░░░ |
| [bandwidth]({{< base >}}html/aP5a38) | █████░░░░ |
| [bipartite number]({{< base >}}html/1dQQ87) | ██░░░░░░░ |
| [bisection bandwidth]({{< base >}}html/wUdmUb) | ████░░░░░ |
| [book thickness]({{< base >}}html/doijTS) | ████░░░░░ |
| [boolean width]({{< base >}}html/A2jPWT) | █████░░░░ |
| [bounded components]({{< base >}}html/t7c4mp) | ███░░░░░░ |
| [boxicity]({{< base >}}html/a7MpiT) | ██████░░░ |
| [branch width]({{< base >}}html/lIcmuR) | ████░░░░░ |
| [c-closure]({{< base >}}html/ou9VU1) | ░░░░░░░░░ |
| [carving-width]({{< base >}}html/dS6OgO) | ███░░░░░░ |
| [chordality]({{< base >}}html/fTqo40) | ████░░░░░ |
| [chromatic number]({{< base >}}html/w7MmyW) | █████░░░░ |
| [clique cover number]({{< base >}}html/VomShB) | █████░░░░ |
| [clique-tree-width]({{< base >}}html/7P9WUz) | ██░░░░░░░ |
| [clique-width]({{< base >}}html/wg5HuV) | ███████░░ |
| [contraction complexity]({{< base >}}html/LlWzhg) | ██░░░░░░░ |
| [cutwidth]({{< base >}}html/TLx1pz) | ████░░░░░ |
| [d-admissibility]({{< base >}}html/Pqiy2C) | ████░░░░░ |
| [d-path-free]({{< base >}}html/s4EiWI) | ██░░░░░░░ |
| [degeneracy]({{< base >}}html/VowkuW) | ██████░░░ |
| [degree treewidth]({{< base >}}html/nCWUh3) | ██████░░░ |
| [diameter]({{< base >}}html/p4bTjp) | ██████░░░ |
| [diameter+max degree]({{< base >}}html/ri9Seh) | ░░░░░░░░░ |
| [distance to bipartite]({{< base >}}html/1yW82F) | █████░░░░ |
| [distance to block]({{< base >}}html/xNJnFb) | ████░░░░░ |
| [distance to bounded components]({{< base >}}html/RPTCxd) | ████░░░░░ |
| [distance to chordal]({{< base >}}html/OdZQna) | ████░░░░░ |
| [distance to cluster]({{< base >}}html/aXw3Co) | █████░░░░ |
| [distance to co-cluster]({{< base >}}html/hbfWwE) | █████░░░░ |
| [distance to cograph]({{< base >}}html/uDXX2i) | █████░░░░ |
| [distance to complete]({{< base >}}html/2LDMQ6) | ██████░░░ |
| [distance to edgeless]({{< base >}}html/4INs10) | █░░░░░░░░ |
| [distance to forest]({{< base >}}html/hQZlLU) | █████░░░░ |
| [distance to interval]({{< base >}}html/AVc2K6) | ███░░░░░░ |
| [distance to linear forest]({{< base >}}html/yk7XP0) | ████░░░░░ |
| [distance to maximum degree]({{< base >}}html/kRR8zx) | ████░░░░░ |
| [distance to outerplanar]({{< base >}}html/lPHVWU) | ███░░░░░░ |
| [distance to perfect]({{< base >}}html/kJZKgd) | ████░░░░░ |
| [distance to planar]({{< base >}}html/MLJMRH) | ████░░░░░ |
| [distance to stars]({{< base >}}html/Z10jME) | ███░░░░░░ |
| [domatic number]({{< base >}}html/KRV6tI) | ███░░░░░░ |
| [domination number]({{< base >}}html/Gq0onN) | ███░░░░░░ |
| [domino treewidth]({{< base >}}html/aEs5ap) | ███░░░░░░ |
| [edge clique cover number]({{< base >}}html/nYQDv6) | ████░░░░░ |
| [edge connectivity]({{< base >}}html/JbqZoT) | ██░░░░░░░ |
| [edge-cut width]({{< base >}}html/ZNqIlN) | ██░░░░░░░ |
| [edge-treewidth]({{< base >}}html/pKi2tL) | ██░░░░░░░ |
| [feedback edge set]({{< base >}}html/HTk9PZ) | ██████░░░ |
| [feedback vertex set]({{< base >}}html/GNOiyB) | ████████░ |
| [flip-width]({{< base >}}html/jYG7BR) | █████░░░░ |
| [genus]({{< base >}}html/gbaHdw) | ██████░░░ |
| [h-index]({{< base >}}html/GNTwUS) | ████░░░░░ |
| [iterated type partitions]({{< base >}}html/G1Cwmc) | ███░░░░░░ |
| [linear clique-width]({{< base >}}html/fQj3wU) | ████░░░░░ |
| [linear NLC-width]({{< base >}}html/v09DMY) | ██░░░░░░░ |
| [linear rank-width]({{< base >}}html/cHugsk) | ██░░░░░░░ |
| [maximum clique]({{< base >}}html/q7zHeT) | █████░░░░ |
| [maximum degree]({{< base >}}html/UyQ5yM) | ████████░ |
| [maximum independent set]({{< base >}}html/mHtXUU) | ██░░░░░░░ |
| [maximum induced matching]({{< base >}}html/GzMYlT) | ███░░░░░░ |
| [maximum leaf number]({{< base >}}html/BN92vX) | ██████░░░ |
| [maximum matching]({{< base >}}html/veU7Jf) | ███░░░░░░ |
| [maximum matching on bipartite graphs]({{< base >}}html/8Mm5qJ) | ░░░░░░░░░ |
| [merge-width]({{< base >}}html/UWmTKl) | █████░░░░ |
| [mim-width]({{< base >}}html/WmIFB1) | ██████░░░ |
| [minimum degree]({{< base >}}html/GPmOeT) | ░░░░░░░░░ |
| [mm-width]({{< base >}}html/d7vRYU) | ████░░░░░ |
| [modular-width]({{< base >}}html/4bj71L) | ███████░░ |
| [module-width]({{< base >}}html/EV3FqL) | ████░░░░░ |
| [neighborhood diversity]({{< base >}}html/vMs3RS) | ██████░░░ |
| [NLC-width]({{< base >}}html/Xrpbv7) | ████░░░░░ |
| [NLCT-width]({{< base >}}html/mOri44) | ██░░░░░░░ |
| [odd cycle transversal]({{< base >}}html/Ve5ruW) | ██████░░░ |
| [overlap treewidth]({{< base >}}html/P8yP3M) | ██░░░░░░░ |
| [pathwidth]({{< base >}}html/VHClqR) | ████████░ |
| [pathwidth+maxdegree]({{< base >}}html/6BWcgd) | ███░░░░░░ |
| [radius-inf flip-width]({{< base >}}html/nYXiuT) | ███░░░░░░ |
| [radius-r flip-width]({{< base >}}html/4DIiH0) | ███░░░░░░ |
| [rank-width]({{< base >}}html/fojquT) | ███████░░ |
| [shrub-depth]({{< base >}}html/NTgNzT) | ██████░░░ |
| [sim-width]({{< base >}}html/aEGv5N) | █████░░░░ |
| [size]({{< base >}}html/F1NpDy) | ███░░░░░░ |
| [slim tree-cut width]({{< base >}}html/oFvl4c) | ██░░░░░░░ |
| [sparse twin-width]({{< base >}}html/2FM8hj) | ██░░░░░░░ |
| [strong coloring number]({{< base >}}html/PxVh3F) | █████░░░░ |
| [strong d-coloring number]({{< base >}}html/yihnem) | ████░░░░░ |
| [strong inf-coloring number]({{< base >}}html/JQTHZS) | ███░░░░░░ |
| [topological bandwidth]({{< base >}}html/SnA7Eq) | ████░░░░░ |
| [tree-cut width]({{< base >}}html/8CgU0P) | ██░░░░░░░ |
| [tree-independence number]({{< base >}}html/fNR6QK) | █████░░░░ |
| [tree-partition-width]({{< base >}}html/QP01gs) | █████░░░░ |
| [treebandwidth]({{< base >}}html/w3LxG1) | ████░░░░░ |
| [treedepth]({{< base >}}html/KEP2qM) | ███████░░ |
| [treelength]({{< base >}}html/JA2nKw) | ██████░░░ |
| [treespan]({{< base >}}html/IbKkUQ) | ███░░░░░░ |
| [treewidth]({{< base >}}html/5Q7fuR) | █████████ |
| [twin-cover number]({{< base >}}html/MUnHA0) | █████░░░░ |
| [twin-width]({{< base >}}html/OrH7et) | ████████░ |
| [vertex connectivity]({{< base >}}html/OyLUe4) | ░░░░░░░░░ |
| [vertex cover]({{< base >}}html/4lp9Yj) | █████████ |
| [vertex integrity]({{< base >}}html/KVhJFB) | ██████░░░ |
| [weak coloring number]({{< base >}}html/KD6n2n) | █████░░░░ |
| [weak d-coloring number]({{< base >}}html/3F3oc3) | ████░░░░░ |
| [weak inf-coloring number]({{< base >}}html/DfwI9E) | ███░░░░░░ |
| [weakly sparse and merge width]({{< base >}}html/HJjpOL) | ░░░░░░░░░ |


---

## Graph classes and Properties

Some parameters are derived from associated graph classes.
Graph classes can be also used as witnesses of proper inclusions.
For these purposes, we use the following graph class hierarchy.
We assume that all of the graph class inclusions are proper.

We aim to have here only the graph classes that influence parameter inclusions.
Please, see [Information System on Graph Classes and their Inclusions (ISGCI)](https://www.graphclasses.org/) for an exhaustive list of graph classes and their inclusions.

### Hasse graphs and properties ([source](graphs.dot))

<p><div id="graphs.dot" class="svg-diagram zoomable"></div></p><script type="module">import { initializeSvgToolbelt } from '/parameters/svg-toolbelt.esm.js';Viz.instance().then(function(viz) {fetch('graphs.dot').then(response => response.text()).then((data) => {var svg = viz.renderSVGElement(data);document.getElementById("graphs.dot").appendChild(svg);initializeSvgToolbelt('.zoomable', {zoomStep: 0.3,minScale: 1,maxScale: 5,});})});</script>



| Graph class | <a href="{{< base >}}docs/legend/#relevance">*</a>Relevance |
| --- | --- |
| [bipartite]({{< base >}}html/cLHJkW) | ████████░ |
| [block]({{< base >}}html/QrxQsH) | ███░░░░░░ |
| [chordal]({{< base >}}html/Cv1PaJ) | ██████░░░ |
| [cluster]({{< base >}}html/WAU7vf) | ██████░░░ |
| [co-cluster]({{< base >}}html/7HR4uV) | ██████░░░ |
| [cograph]({{< base >}}html/9Qd0Mx) | ███████░░ |
| [complete]({{< base >}}html/EhdXNA) | █████████ |
| [cycle]({{< base >}}html/Ti0asF) | ██░░░░░░░ |
| [cycles]({{< base >}}html/2iJr52) | ████░░░░░ |
| [forest]({{< base >}}html/JngPPm) | █████████ |
| [grid]({{< base >}}html/lfYXuK) | ██████░░░ |
| [interval]({{< base >}}html/p5skoj) | ███████░░ |
| [linear forest]({{< base >}}html/skQuFN) | ████░░░░░ |
| [outerplanar]({{< base >}}html/0oCyaG) | █████░░░░ |
| [path]({{< base >}}html/ryPlqz) | ███░░░░░░ |
| [perfect]({{< base >}}html/RmssrZ) | ██████░░░ |
| [planar]({{< base >}}html/loZ5LD) | ████████░ |
| [series-parallel]({{< base >}}html/eW1Gic) | ██████░░░ |
| [star]({{< base >}}html/CortlU) | ███░░░░░░ |
| [stars]({{< base >}}html/10JR3F) | ████░░░░░ |
| [tree]({{< base >}}html/rJyICu) | ███████░░ |


| Property | <a href="{{< base >}}docs/legend/#relevance">*</a>Relevance |
| --- | --- |
| [bounded expansion]({{< base >}}html/lFz6Ci) | ██████░░░ |
| [chi-bounded]({{< base >}}html/Jb1we5) | █████░░░░ |
| [connected]({{< base >}}html/KlMP0i) | ██░░░░░░░ |
| [edgeless]({{< base >}}html/LsiBbX) | █░░░░░░░░ |
| [excluded minor]({{< base >}}html/5xOuoQ) | ████░░░░░ |
| [excluded planar minor]({{< base >}}html/Gt22Ik) | ████░░░░░ |
| [excluded top-minor]({{< base >}}html/yOZQM5) | ███░░░░░░ |
| [monadically dependent]({{< base >}}html/dN1D3C) | █████░░░░ |
| [monadically stable]({{< base >}}html/jHXy6Y) | █████░░░░ |
| [nowhere dense]({{< base >}}html/DhGqJM) | █████░░░░ |
| [weakly sparse]({{< base >}}html/Qme7wD) | ███░░░░░░ |


---

## Sources

* [download .bib file for all the sources](../main.bib)

| # | Year | <a href="{{< base >}}docs/legend/#relevance">*</a>Relevance | Source |
| --- | --- | --- | --- |
| 000 | 2025 | ████░░░░░ | [On a tree-based variant of bandwidth and forbidding simple topological minors by Jacob, Lochet, Paul]({{< base >}}html/EImlRb) |
| 001 | 2024 | ███░░░░░░ | [Parameterized complexity for iterated type partitions and modular-width by Cordasco, Gargano, Rescigno]({{< base >}}html/oBcMqr) |
| 002 | 2024 | ██░░░░░░░ | [Twin-width of graphs on surfaces by Kráľ, Pekárková, Štorgel]({{< base >}}html/lgJ2j7) |
| 003 | 2023 | █░░░░░░░░ | [On Algorithmic Applications of Sim-Width and Mim-Width of $(H_1,H_2)$-Free Graphs by Munaro, Yang]({{< base >}}html/47Xy7Z) |
| 004 | 2024 | ███████░░ | [Merge-width and First-Order Model Checking by Dreier, Toruńczyk]({{< base >}}html/9exguJ) |
| 005 | 2024 | █████░░░░ | [Slim Tree-Cut Width by Ganian, Korchemna]({{< base >}}html/7g1aTu) |
| 006 | 2023 | ███████░░ | [Flip-width: Cops and Robber on dense graphs by Toruńczyk]({{< base >}}html/KpkMZB) |
| 007 | 2022 | ███████░░ | [Expanding the Graph Parameter Hierarchy by Tran]({{< base >}}html/uXViPE) |
| 008 | 2022 | ████░░░░░ | [Edge-Cut Width: An Algorithmically Driven Analogue of Treewidth Based on Edge Cuts by Brand, Ceylan, Ganian, Hatschka, Korchemna]({{< base >}}html/xhGnnq) |
| 009 | 2021 | ██████░░░ | [Twin-width I: Tractable `FO` Model Checking by Bonnet, Kim, Thomassé, Watrigant]({{< base >}}html/nyaOye) |
| 010 | 2022 | ██████░░░ | [Excluding a Ladder by Huynh, Joret, Micek, Seweryn, Wollan]({{< base >}}html/EdPIVj) |
| 011 | unknown | ███████░░ | [Comparing Graph Parameters by Schröder]({{< base >}}html/DYGiYb) |
| 012 | 2020 | █░░░░░░░░ | [Mim-Width I. Induced path problems by Jaffke, Kwon, Telle]({{< base >}}html/BIQh3r) |
| 013 | 2019 | ███████░░ | [The Graph Parameter Hierarchy by Sorge]({{< base >}}html/VnTIL0) |
| 014 | 2019 | █████░░░░ | [Shrub-depth: Capturing Height of Dense Graphs by Ganian, Hliněný, Nešetřil, Obdržálek, Ossona de Mendez]({{< base >}}html/Scw7zm) |
| 015 | 2018 | █░░░░░░░░ | [A systematic comparison of graph parameters by Frömmrich]({{< base >}}html/45xW87) |
| 016 | 2017 | ███████░░ | [Graph Theory by Diestel]({{< base >}}html/r2Lwky) |
| 017 | 2015 | █████████ | [Parameterized Algorithms by Cygan, Fomin, Kowalik, Lokshtanov, Marx, Pilipczuk, Pilipczuk, Saurabh]({{< base >}}html/Xlsyce) |
| 018 | 2015 | ████░░░░░ | [Improving Vertex Cover as a Graph Parameter by Ganian]({{< base >}}html/VQLE2i) |
| 019 | 2015 | ██░░░░░░░ | [Linear rank-width and linear clique-width of trees by Adler, Kanté]({{< base >}}html/rhj9my) |
| 020 | 2015 | ███░░░░░░ | [The structure of graphs not admitting a fixed immersion by Wollan]({{< base >}}html/zbWWC6) |
| 021 | 2013 | █░░░░░░░░ | [The Power of Data Reduction: Kernels for Fundamental Graph Problems by Jansen]({{< base >}}html/FLOjic) |
| 022 | 2013 | █░░░░░░░░ | [Characterizing graphs of small carving-width by Belmonte, van 't Hof, Kamiński, Paulusma, Thilikos]({{< base >}}html/sJ476m) |
| 023 | 2013 | ███░░░░░░ | [Parameterized Algorithms for Modular-Width by Gajarský, Lampis, Ordyniak]({{< base >}}html/OH3sI3) |
| 024 | 2012 | ███░░░░░░ | [New Width Parameters of Graphs by Vatshelle]({{< base >}}html/nRO7AG) |
| 025 | 2012 | ████░░░░░ | [Twin-Cover: Beyond Vertex Cover in Parameterized Algorithmics by Ganian]({{< base >}}html/7UoBR6) |
| 026 | 2012 | ████░░░░░ | [Classes of graphs with small rank decompositions are χ-bounded by Dvořák, Král’]({{< base >}}html/DbAWDM) |
| 027 | 2012 | █░░░░░░░░ | [Algorithmic Meta-theorems for Restrictions of Treewidth by Lampis]({{< base >}}html/0LYUEV) |
| 028 | 2011 | ████░░░░░ | [Boolean-width of graphs by Bui-Xuan, Telle, Vatshelle]({{< base >}}html/cNjhWx) |
| 029 | 2011 | ██░░░░░░░ | [Chordal Bipartite Graphs with High Boxicity by Chandran, Francis, Mathew]({{< base >}}html/Vkc4EU) |
| 030 | 2010 | ███████░░ | [Comparing 17 graph parameters by Sasák]({{< base >}}html/XlBXyo) |
| 031 | 2010 | █░░░░░░░░ | [The rank-width of the square grid by Jelínek]({{< base >}}html/vIBI5v) |
| 032 | 2009 | ███░░░░░░ | [On tree-partition-width by Wood]({{< base >}}html/p00uyg) |
| 033 | 2009 | ██░░░░░░░ | [Clique-Width is `NP`-Complete by Fellows, Rosamond, Rotics, Szeider]({{< base >}}html/zuhSo5) |
| 034 | 2008 | ███░░░░░░ | [Grad and classes with bounded expansion II. Algorithmic aspects by Nešetřil, Ossona de Mendez]({{< base >}}html/kXDDmb) |
| 035 | 2008 | ██░░░░░░░ | [Spanning Trees with Many Leaves and Average Distance by DeLaViña, Waller]({{< base >}}html/C5cBsd) |
| 036 | 2008 | ██░░░░░░░ | [Simulating Quantum Computation by Contracting Tensor Networks by Markov, Shi]({{< base >}}html/9JAQC7) |
| 037 | 2007 | ████░░░░░ | [Graph Treewidth and Geometric Thickness Parameters by Dujmovic, Wood]({{< base >}}html/2q7m9E) |
| 038 | 2006 | ████░░░░░ | [Approximating clique-width and branch-width by Oum, Seymour]({{< base >}}html/1ZTWBd) |
| 039 | 2005 | ███░░░░░░ | [On the relationship between NLC-width and linear NLC-width by Gurski, Wanke]({{< base >}}html/FLSQsw) |
| 040 | 2005 | ████░░░░░ | [Graph Searching, Elimination Trees, and a Generalization of Bandwidth by Fomin, Heggernes, Telle]({{< base >}}html/mIg9Mh) |
| 041 | 2004 | ███░░░░░░ | [Track Layouts of Graphs by Dujmović, Pór, Wood]({{< base >}}html/w7RVn9) |
| 042 | 2000 | █████░░░░ | [Upper bounds to the clique width of graphs by Courcelle, Olariu]({{< base >}}html/ZQrXS8) |
| 043 | 1999 | ████░░░░░ | [A note on domino treewidth by Bodlaender]({{< base >}}html/gcMYuX) |
| 044 | 1998 | ███░░░░░░ | [Clique-decomposition, NLC-decomposition and modular decomposition—relationships and results for random graphs by Johansson]({{< base >}}html/W2nwG4) |
| 045 | 1998 | ██████░░░ | [A partial $k$-arboretum of graphs with bounded treewidth by Bodlaender]({{< base >}}html/BOFCWg) |
| 046 | 1997 | █████░░░░ | [Domino Treewidth by Bodlaender, Engelfriet]({{< base >}}html/SN1KnV) |
| 047 | 1994 | ███░░░░░░ | [k-NLC graphs and polynomial algorithms by Wanke]({{< base >}}html/SQjcYg) |
| 048 | 1993 | █████░░░░ | [The Pathwidth and Treewidth of Cographs by Bodlaender, Möhring]({{< base >}}html/a3yKzk) |
| 049 | 1991 | ███████░░ | [Graph minors. X. Obstructions to tree-decomposition by Robertson, Seymour]({{< base >}}html/1hPzXs) |
| 050 | 1986 | ███░░░░░░ | [Graph minors. V. Excluding a planar graph by Robertson, Seymour]({{< base >}}html/A82svt) |
| 051 | 1994 | ██░░░░░░░ | [Genus $g$ Graphs Have Pagenumber $O(\sqrt g)$ by Malitz]({{< base >}}html/cCrsoK) |
| 052 | 1993 | ████░░░░░ | [On the chordality of a graph by McKee, Scheinerman]({{< base >}}html/IFY0Rw) |
| 053 | 1989 | ███░░░░░░ | [On dimensional properties of graphs by Cozzens, Roberts]({{< base >}}html/hEmGQO) |
| 054 | 1986 | ████████░ | [Graph minors. II. Algorithmic aspects of tree-width by Robertson, Seymour]({{< base >}}html/i56ihO) |
| 055 | 1988 | █░░░░░░░░ | [The average distanceisnot morethan the independence number by Chung]({{< base >}}html/ePpmZt) |
| 056 | 1985 | █░░░░░░░░ | [On the Cutwidth and the Topological Bandwidth of a Tree by Chung]({{< base >}}html/DkY1Aq) |


---

## Tags

* [topology]({{< base >}}html/lJJaYb)
* [coloring]({{< base >}}html/szWO2M)
* [vertex removal]({{< base >}}html/e26LM8)
* [edge removal]({{< base >}}html/hnX8tG)
* [covering edges]({{< base >}}html/tK4S1r)
* [covering vertices]({{< base >}}html/TgTiqK)
* [vertex order]({{< base >}}html/O1poSV)
* [module]({{< base >}}html/ZtdvKW)
* [linear variant]({{< base >}}html/nAjQi4)
* [tree decomposition]({{< base >}}html/bzffn0)
* [branch decomposition]({{< base >}}html/KaLXjx)
* [intersection]({{< base >}}html/QqAXvX)



