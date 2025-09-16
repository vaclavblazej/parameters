# New Width Parameters of Graphs by Vatshelle

[https://hdl.handle.net/1956/6166](https://hdl.handle.net/1956/6166)

```bibtex
@thesis{Vatshelle2012,
author = {Martin Vatshelle},
isbn = {978-82-308-2098-8},
publisher = {The University of Bergen},
title = {New Width Parameters of Graphs},
url = {https://hdl.handle.net/1956/6166},
year = {2012},
}
```
* page 33 : [mm-width]({{< base >}}html/d7vRYU) -- Definition 3.6.1 (MM-width). For $G$ a graph and $A \subseteq V(G)$ let $mm \colon 2^{V(G)} \to \mathbb N$ be a function where $mm(A)$ for $A \subseteq V(G)$ is the size of a maximum matching in $G[A,\bar A]$. Using Definition 3.1.3 with $f=mm$ we define $mmw(T,\delta)$ as the $f$-width of a binary decomposition tree $(T,\delta)$ and $mmw(G)$ as the $f$-width of $G$, also called the MM-width of $G$ or the maximum matching width.
* page 33 : [mim-width]({{< base >}}html/WmIFB1) -- Definition 3.7.1 (MIM-width). For $G$ a graph and $A \subseteq V(G)$ let $mim \colon 2^{V(G)} \to \mathbb N$ be a function where $mim(A)$ is the size of a maximum induced matching in $G[A,\bar A]$. Using Definition 3.1.3 with $f=mim$ we define $mimw(T,\delta)$ as the $f$-width of a binary decomposition tree $(T,\delta)$ and $mimw(G)$ as the $f$-width of $G$, also called the MIM-width of $G$ or the maximum induced matching width.
* page 40 : [treewidth]({{< base >}}html/5Q7fuR) upper bounds [mm-width]({{< base >}}html/d7vRYU) by a linear function -- Theorem 4.2.5. Let $G$ be a graph, then $\frac 13 (tw(G)+1) \le mmw(G) \le \max(brw(G),1) \le tw(G)+1$
* page 40 : [mm-width]({{< base >}}html/d7vRYU) upper bounds [treewidth]({{< base >}}html/5Q7fuR) by a linear function -- Theorem 4.2.5. Let $G$ be a graph, then $\frac 13 (tw(G)+1) \le mmw(G) \le \max(brw(G),1) \le tw(G)+1$
* page 42 : [boolean width]({{< base >}}html/A2jPWT) upper bounds [mim-width]({{< base >}}html/WmIFB1) by a linear function -- Theorem 4.2.10. Let $G$ be a graph, then $mimw(G) \le boolw(G) \le mimw(G) \log_2(n)$