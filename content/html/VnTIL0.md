# The Graph Parameter Hierarchy by Sorge

[https://manyu.pro/assets/parameter-hierarchy.pdf](https://manyu.pro/assets/parameter-hierarchy.pdf)

```bibtex
@unpublished{Sorge2019,
author = {Manuel Sorge},
title = {The Graph Parameter Hierarchy},
url = {https://manyu.pro/assets/parameter-hierarchy.pdf},
year = {2019},
}
```
<p><div id="../drawing_VnTIL0_0.dot" class="svg-diagram zoomable"></div></p><script type="module">import { initializeSvgToolbelt } from 'http://localhost:1313/parameters/svg-toolbelt.esm.js';Viz.instance().then(function(viz) {fetch('../drawing_VnTIL0_0.dot').then(response => response.text()).then((data) => {var svg = viz.renderSVGElement(data);document.getElementById("../drawing_VnTIL0_0.dot").appendChild(svg);initializeSvgToolbelt('.zoomable', {zoomStep: 0.3,minScale: 1,maxScale: 5,});})});</script>

* page 3 : [acyclic chromatic number]({{< base >}}html/QGZuUW) -- The \emph{acyclic chromatic number} of a graph $G = (V,E)$ is the smallest size of a vertex partition $P=\{V_1,\dots,V_\ell\}$ such that each $V_i$ is an independent set and for all $V_i,V_j$ the graph $G[V_i \cup V_j]$ does not contain a cycle.
* page 3 : [arboricity]({{< base >}}html/zgMenA) -- The \emph{arboricity} of a graph $G$ is the minimum number of forests the edges of $G$ can be partitioned into.
* page 3 : [average degree]({{< base >}}html/z0y4TW) -- The \emph{average degree} of a graph $G = (V,E)$ is $2|E|/|V|$.
* page 8 : [arboricity]({{< base >}}html/zgMenA) upper bounds [degeneracy]({{< base >}}html/VowkuW) by a linear function -- Lemma 4.5
* page 8 : [degeneracy]({{< base >}}html/VowkuW) upper bounds [arboricity]({{< base >}}html/zgMenA) by a linear function -- Lemma 4.5
* page 8 : [maximum degree]({{< base >}}html/UyQ5yM) upper bounds [acyclic chromatic number]({{< base >}}html/QGZuUW) by a polynomial function -- Lemma 4.6 ([15]). The acyclic chromatic number $\chi_a$ is uppre bounded by the maximum degree $\Delta$ (for every graph with $\Delta > 4$). We have $\chi_a \le \Delta(\Delta-1)/2$.
* page 8 : [h-index]({{< base >}}html/GNTwUS) upper bounds [acyclic chromatic number]({{< base >}}html/QGZuUW) by a polynomial function -- Lemma 4.7. The acyclic chromatic number $\chi_a$ is upper bounded by the $h$-index $h$. We have $\chi_a \le h(h+1)/2$.
* page 8 : [genus]({{< base >}}html/gbaHdw) upper bounds [acyclic chromatic number]({{< base >}}html/QGZuUW) by a linear function -- Lemma 4.8 ([3]). The accylic chromatic number $\chi_a$ is upper bounded by the genus $g$. We have $\chi_a \le 4g+4$.
* page 8 : [acyclic chromatic number]({{< base >}}html/QGZuUW) upper bounds [boxicity]({{< base >}}html/a7MpiT) by a computable function -- Lemma 4.9. The boxicity $b$ is upper bounded by the acyclic chromatic number $\chi_a$ (for every graph with $\chi_a>1$). We have $b \le \chi_a(\chi_a-1)$.
* page 8 : [maximum leaf number]({{< base >}}html/BN92vX) upper bounds [distance to linear forest]({{< base >}}html/yk7XP0) by a computable function -- Lemma 4.10 ([14]). The max-leaf number $\mathrm{ml}$ upper bounds the distance to disjoint paths $d$. We have $d \le \mathrm{ml}-1$.
* page 9 : [boxicity]({{< base >}}html/a7MpiT) upper bounds [chordality]({{< base >}}html/fTqo40) by a linear function -- Lemma 4.15 ([8,11]). The boxicity $b$ upper-bounds the chordality $c$. We have $c \le b$.
* page 9 : [distance to interval]({{< base >}}html/AVc2K6) upper bounds [boxicity]({{< base >}}html/a7MpiT) by a linear function -- Lemma 4.16. The distance $i$ to an interval graph upper bounds the boxicity $b$. We have $b \le i+1$.
* page 9 : [distance to chordal]({{< base >}}html/OdZQna) upper bounds [chordality]({{< base >}}html/fTqo40) by a linear function -- (ed: apparently goes as the lemma for ddist to interval and boxicity) Lemma 4.16. The distance $i$ to an interval graph upper bounds the boxicity $b$. We have $b \le i+1$.
* page 9 : [distance to cograph]({{< base >}}html/uDXX2i) upper bounds [clique-width]({{< base >}}html/wg5HuV) by an exponential function -- Lemma 4.17. The distance $c$ to a cograph upper bounds the cliquewidth $q$. We have $q \le 2^{3+c}-1$.
* page 9 : [acyclic chromatic number]({{< base >}}html/QGZuUW) upper bounds [degeneracy]({{< base >}}html/VowkuW) by a polynomial function -- Lemma 4.18. The acyclic chromatic number $a$ upper bounds the degeneracy $d$. We have $d \le 2 \binom a2 - 1$
* page 10 : [feedback edge set]({{< base >}}html/HTk9PZ) upper bounds [genus]({{< base >}}html/gbaHdw) by a linear function -- Lemma 4.19. The feedback edge set number $f$ upper bounds the genus $g$. We have $g \le f$.
* page 10 : [feedback vertex set]({{< base >}}html/GNOiyB) upper bounds [distance to chordal]({{< base >}}html/OdZQna) by a linear function -- Lemma 4.20. The feedback edge set number $f$ upper bounds the distance to a chordal graph $c$. We have $c \le f$.
* page 10 : [maximum leaf number]({{< base >}}html/BN92vX) upper bounds [bandwidth]({{< base >}}html/aP5a38) by a linear function -- Lemma 4.25. The max leaf number $\mathrm{ml}$ strictly upper bounds the bandwidth $\mathrm{bw}$.
* page 11 : [clique cover number]({{< base >}}html/VomShB) upper bounds [maximum independent set]({{< base >}}html/mHtXUU) by a linear function -- Lemma 4.26. The minimum clique cover number $c$ strictly upper bounds the independence number $\alpha$.
* page 11 : [treedepth]({{< base >}}html/KEP2qM) upper bounds [pathwidth]({{< base >}}html/VHClqR) by a linear function -- Lemma 4.27. The treedepth $t$ strictly upper bounds the pathwidth $p$. We have $p \le t$.