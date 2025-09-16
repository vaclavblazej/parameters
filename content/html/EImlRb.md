# On a tree-based variant of bandwidth and forbidding simple topological minors by Jacob, Lochet, Paul

[https://arxiv.org/abs/2502.11674v1](https://arxiv.org/abs/2502.11674v1)

```bibtex
@misc{treebandwidth2025,
archiveprefix = {arXiv},
author = {Hugo Jacob and William Lochet and Christophe Paul},
eprint = {2502.11674},
primaryclass = {cs.DM},
title = {On a tree-based variant of bandwidth and forbidding simple topological minors},
url = {https://arxiv.org/abs/2502.11674v1},
year = {2025},
}
```
<p><div id="../drawing_EImlRb_0.dot" class="svg-diagram zoomable"></div></p><script type="module">import { initializeSvgToolbelt } from '/parameters/svg-toolbelt.esm.js';Viz.instance().then(function(viz) {fetch('../drawing_EImlRb_0.dot').then(response => response.text()).then((data) => {var svg = viz.renderSVGElement(data);document.getElementById("../drawing_EImlRb_0.dot").appendChild(svg);initializeSvgToolbelt('.zoomable', {zoomStep: 0.3,minScale: 1,maxScale: 5,});})});</script>

* page 1 : [treebandwidth]({{< base >}}html/w3LxG1) -- A \emph{tree-layout} of $G=(V,E)$ is a rooted tree $T$ whose nodes are the vertices of $V$, and such that, for every edge $xy \in E$, $x$ is an ancestor of $y$ or vice-versa. The bandwidth of $T$ is then the maximum distance in $T$ between pairs of neighbors in $G$. We call \emph{treebandwidth} of $G$, the minimum bandwidth over tree-layouts of $G$, and denote it by ${\rm tbw}(G)$.
* page 7 : [tree-partition-width]({{< base >}}html/QP01gs) upper bounds [treebandwidth]({{< base >}}html/w3LxG1) by a linear function -- By rooting the tree-partition arbitrarily and replacing each bag by an arbitrary linear ordering of its vertices one derives ${\rm tbw}(G) \le 2 \cdot {\rm tpw}(G)$. However, some graphs of treebandwidth 2 have unbounded tree-partition-width: ...
* page 7 : graph classes with bounded [treebandwidth]({{< base >}}html/w3LxG1) are not bounded [tree-partition-width]({{< base >}}html/QP01gs) -- By rooting the tree-partition arbitrarily and replacing each bag by an arbitrary linear ordering of its vertices one derives ${\rm tbw}(G) \le 2 \cdot {\rm tpw}(G)$. However, some graphs of treebandwidth 2 have unbounded tree-partition-width: ...
* page 36 : [vertex cover]({{< base >}}html/4lp9Yj) upper and lower bounds [maximum matching]({{< base >}}html/veU7Jf) by a linear function -- ... discovered independently by Fanica Gavril and Mihalis Yannakakis. Theorem 50. In a graph $G$, we have $\mu(G) \le {\rm vc}(G) \le 2\mu(G)$, where $\mu(G)$ is the maximum matching number of $G$.
* page 36 : [maximum matching]({{< base >}}html/veU7Jf) upper bounds [vertex cover]({{< base >}}html/4lp9Yj) by a linear function -- ... discovered independently by Fanica Gavril and Mihalis Yannakakis. Theorem 50. In a graph $G$, we have $\mu(G) \le {\rm vc}(G) \le 2\mu(G)$, where $\mu(G)$ is the maximum matching number of $G$.
* page 37 : [degree treewidth]({{< base >}}html/nCWUh3) upper bounds [domino treewidth]({{< base >}}html/aEs5ap) by a linear function -- Theorem 53. ... $\max({\rm tw}(G),(\Delta(G)-1)/2) \le {\rm dtw}(G)$ ... [this result is claimed to be in [A note on domino treewidth by Bodlaender]({{< base >}}html/gcMYuX), didn't see it there]
* page 37 : [treespan]({{< base >}}html/IbKkUQ) upper bounds [degree treewidth]({{< base >}}html/nCWUh3) by a linear function -- Claim 55. $\max({\rm tw}(G),\Delta(G)/2) \le {\rm ts}(G)$
* page 38 : [domino treewidth]({{< base >}}html/aEs5ap) upper bounds [treespan]({{< base >}}html/IbKkUQ) by a linear function -- Claim 56. ${\rm ts}(G)$ \le 2 \cdot {\rm dtw}(G)
* page 38 : [treebandwidth]({{< base >}}html/w3LxG1) upper bounds [treewidth]({{< base >}}html/5Q7fuR) by a computable function -- [implied through obstructions]