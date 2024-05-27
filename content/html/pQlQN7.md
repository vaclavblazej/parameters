# Unknown pQlQN7

* [linear forest]({{< base >}}html/skQuFN) -- Disjoint union of paths.
* [vertex cover]({{< base >}}html/4lp9Yj) equal to $k$ implies that [maximum matching]({{< base >}}html/veU7Jf) is upper bounded by $\mathcal O(k)$
* [odd cycle transversal]({{< base >}}html/Ve5ruW) is equal to [distance to bipartite]({{< base >}}html/distance_to_cLHJkW) -- Bipartite graphs is the graph class without any odd cycles.
* [feedback edge set]({{< base >}}html/HTk9PZ) equal to $k$ implies that [feedback vertex set]({{< base >}}html/GNOiyB) is upper bounded by $\mathcal O(k)$ -- Given solution to feedback edge set one can remove one vertex incident to the solution edges to obtain feedback vertex set.
* [feedback edge set]({{< base >}}html/HTk9PZ) equal to $k$ implies that [genus]({{< base >}}html/gbaHdw) is upper bounded by $\mathcal O(k)$ -- Removing $k$ edges creates a forest that is embeddable into the plane. We now add one handle for each of the $k$ edges to get embedding into $k$-handle genus.
* [chromatic number]({{< base >}}html/w7MmyW) equal to $k$ implies that [maximum clique]({{< base >}}html/q7zHeT) is upper bounded by $\mathcal O(k)$ -- Unbounded clique implies the number of needed colors is unbounded.
* [degeneracy]({{< base >}}html/VowkuW) equal to $k$ implies that [chromatic number]({{< base >}}html/w7MmyW) is upper bounded by $\mathcal O(k)$ -- Greedily color the vertices in order of the degeneracy ordering. As each vertex has at most $k$ colored predecesors we use at most $k+1$ colors.
* [degeneracy]({{< base >}}html/VowkuW) equal to $k$ implies that [average degree]({{< base >}}html/z0y4TW) is upper bounded by $\mathcal O(k)$ -- Removing a vertex of degree $d$ increases the value added to the sum of all degrees by at most $2d$, hence, the average is no more than twice the degeneracy.
* [maximum degree]({{< base >}}html/UyQ5yM) equal to $k$ implies that [h-index]({{< base >}}html/GNTwUS) is upper bounded by $\mathcal O(k)$ -- As h-index seeks $k$ vertices of degree $k$ it is trivially upper bound by maximum degree.
* [minimum degree]({{< base >}}html/GPmOeT) equal to $k$ implies that [edge connectivity]({{< base >}}html/JbqZoT) is upper bounded by $\mathcal O(k)$ -- Removing edges incident to the minimum degree vertex disconnects the graph.
* [linear rank width]({{< base >}}html/cHugsk) equal to $k$ implies that [rank width]({{< base >}}html/fojquT) is upper bounded by $f(k)$
* [pathwidth]({{< base >}}html/VHClqR) equal to $k$ implies that [linear rank width]({{< base >}}html/cHugsk) is upper bounded by $f(k)$
* [minimum degree]({{< base >}}html/GPmOeT) equal to $k$ implies that [domatic number]({{< base >}}html/KRV6tI) is upper bounded by $\mathcal O(k)$ -- The vertex of minimum degree needs to be dominated in each of the sets. As the sets cannot overlap there can be at most $k+1$ of them.
* [distance to linear forest]({{< base >}}html/distance_to_skQuFN) equal to $k$ implies that [pathwidth]({{< base >}}html/VHClqR) is upper bounded by $\mathcal O(k)$ -- After removal of $k$ vertices the remaining class has a bounded width $w$. So by including the removed vertices in every bag, we can achieve decomposition of width $w+k$
* [topological bandwidth]({{< base >}}html/SnA7Eq) equal to $k$ implies that [bisection bandwidth]({{< base >}}html/wUdmUb) is upper bounded by $\mathcal O(k)$ -- Order vertices by their bandwidth integer. We split the graph in the middle of this ordering. There are at most roughly $k^2/2$ edges over this split.
* [bandwidth]({{< base >}}html/aP5a38) equal to $k$ implies that [maximum degree]({{< base >}}html/UyQ5yM) is upper bounded by $\mathcal O(k)$ -- Each vertex has an integer $i$ and may be connected only to vertices whose difference from $i$ is at most $k$. There are at most $k$ bigger and $k$ smaller such neighbors.
* [distance to linear forest]({{< base >}}html/distance_to_skQuFN) equal to $k$ implies that [pathwidth]({{< base >}}html/VHClqR) is upper bounded by $\mathcal O(k)$ -- After removal of $k$ vertices the remaining class has a bounded width $w$. So by including the removed vertices in every bag, we can achieve decomposition of width $w+k$
* [distance to outerplanar]({{< base >}}html/distance_to_0oCyaG) equal to $k$ implies that [treewidth]({{< base >}}html/5Q7fuR) is upper bounded by $\mathcal O(k)$ -- After removal of $k$ vertices the remaining class has a bounded width $w$. So by including the removed vertices in every bag, we can achieve decomposition of width $w+k$
* [vertex integrity]({{< base >}}html/KVhJFB) equal to $k$ implies that [treedepth]({{< base >}}html/KEP2qM) is upper bounded by $\mathcal O(k)$ -- First, treedepth removes vertices of the modulator, then it iterates through remaining components one by one.
* [distance to constant components]({{< base >}}html/distance_to_FJ8gmU) equal to $k$ implies that [vertex integrity]({{< base >}}html/KVhJFB) is upper bounded by $\mathcal O(k)$ -- The remaining components in vertex integrity are parameter-sized which can be always made bigger than constant-sized components.
* [distance to stars]({{< base >}}html/distance_to_10JR3F) equal to $k$ implies that [treedepth]({{< base >}}html/KEP2qM) is upper bounded by $\mathcal O(k)$ -- First, treedepth removes vertices of the modulator, remainder has treedepth $2$
* [distance to complete]({{< base >}}html/distance_to_EhdXNA) equal to $k$ implies that [clique cover number]({{< base >}}html/VomShB) is upper bounded by $\mathcal O(k)$ -- We cover the $k$ vertices of the modulator by cliques of size $1$ and cover the remaining clique by another one.
* [maximum independent set]({{< base >}}html/mHtXUU) equal to $k$ implies that [domination number]({{< base >}}html/Gq0onN) is upper bounded by $\mathcal O(k)$ -- Every maximal independent set is also a dominating set because any undominated vertex could be added to the independent set.
* [domination number]({{< base >}}html/Gq0onN) equal to $k$ implies that [diameter]({{< base >}}html/p4bTjp) is upper bounded by $\mathcal O(k)$ -- An unbounded diameter implies a long path where no vertices that are more than $3$ apart may be dominated by the same dominating vertex, otherwise we could shorten the path. Hence, the number of dominating vertices is also unbounded.
* [distance to bipartite]({{< base >}}html/distance_to_cLHJkW) equal to $k$ implies that [chromatic number]({{< base >}}html/w7MmyW) is upper bounded by $\mathcal O(k)$ -- Removed vertices get one color each and we need only $2$ colors for the rest.
* [edge clique cover number]({{< base >}}html/nYQDv6) equal to $k$ implies that [neighborhood diversity]({{< base >}}html/vMs3RS) is upper bounded by $2^{\mathcal O(k)}$ -- Label vertices by the cliques they are contained in, each label is its own group in the neighborhood diversity, connect accordingly.
* [distance to complete]({{< base >}}html/distance_to_EhdXNA) equal to $k$ implies that [edge clique cover number]({{< base >}}html/nYQDv6) is upper bounded by $k^{\mathcal O(1)}$ -- Cover the remaining clique, cover each modulator vertex and its neighborhood outside of it with another clique, cover each edge within the modulator by its own edge.
* [treewidth]({{< base >}}html/5Q7fuR) equal to $k$ implies that [book thickness]({{< base >}}html/doijTS) is upper bounded by $f(k)$
* [chromatic number]({{< base >}}html/w7MmyW) equal to $k$ implies that [chordality]({{< base >}}html/fTqo40) is upper bounded by $f(k)$
* [maximum leaf number]({{< base >}}html/BN92vX) equal to $k$ implies that [distance to linear forest]({{< base >}}html/distance_to_skQuFN) is upper bounded by $f(k)$
* [genus]({{< base >}}html/gbaHdw) equal to $k$ implies that [book thickness]({{< base >}}html/doijTS) is upper bounded by $f(k)$
* [acyclic chromatic number]({{< base >}}html/QGZuUW) equal to $k$ implies that [boxicity]({{< base >}}html/a7MpiT) is upper bounded by $f(k)$
* [h-index]({{< base >}}html/GNTwUS) equal to $k$ implies that [distance to maximum degree]({{< base >}}html/distance_to_UyQ5yM) is upper bounded by $\mathcal O(k)$ -- Remove the $h$ vertices of degree at least $h$ to get a graph that has maximum degree $h$.
* [distance to maximum degree]({{< base >}}html/distance_to_UyQ5yM) equal to $k$ implies that [h-index]({{< base >}}html/GNTwUS) is upper bounded by $\mathcal O(k)$ -- Removal of $k$ vertices yielding a graph with maximum degree $c$ means that there were $k$ vertices of arbitrary degree and the remaining vertices had degree at most $k+c$. Hence, $h$-index is no more than $k+c$.
* [distance to chordal]({{< base >}}html/distance_to_Cv1PaJ) equal to $k$ implies that [chordality]({{< base >}}html/fTqo40) is upper bounded by $f(k)$
* [distance to cograph]({{< base >}}html/distance_to_9Qd0Mx) equal to $k$ implies that [clique width]({{< base >}}html/wg5HuV) is upper bounded by $f(k)$
* [distance to cograph]({{< base >}}html/distance_to_9Qd0Mx) equal to $k$ implies that [chordality]({{< base >}}html/fTqo40) is upper bounded by $f(k)$
* [distance to cograph]({{< base >}}html/distance_to_9Qd0Mx) equal to $k$ implies that [diameter]({{< base >}}html/p4bTjp) is upper bounded by $f(k)$
* [book thickness]({{< base >}}html/doijTS) equal to $k$ implies that [acyclic chromatic number]({{< base >}}html/QGZuUW) is upper bounded by $f(k)$
* [distance to planar]({{< base >}}html/distance_to_loZ5LD) equal to $k$ implies that [acyclic chromatic number]({{< base >}}html/QGZuUW) is upper bounded by $f(k)$
* [average distance]({{< base >}}html/zH8PpT) equal to $k$ implies that [girth]({{< base >}}html/BCwUeT) is upper bounded by $f(k)$
* [maximum leaf number]({{< base >}}html/BN92vX) equal to $k$ implies that [feedback edge set]({{< base >}}html/HTk9PZ) is upper bounded by $f(k)$
* [maximum induced matching]({{< base >}}html/GzMYlT) equal to $k$ implies that [diameter]({{< base >}}html/p4bTjp) is upper bounded by $f(k)$
* [maximum independent set]({{< base >}}html/mHtXUU) equal to $k$ implies that [maximum induced matching]({{< base >}}html/GzMYlT) is upper bounded by $f(k)$
* [vertex cover]({{< base >}}html/4lp9Yj) equal to $k$ implies that [neighborhood diversity]({{< base >}}html/vMs3RS) is upper bounded by $2^{\mathcal O(k)}$
* bounded [twin-cover number]({{< base >}}html/MUnHA0) does not imply bounded [neighborhood diversity]({{< base >}}html/vMs3RS)
* [linear clique-width]({{< base >}}html/fQj3wU) equal to $k$ implies that [clique width]({{< base >}}html/wg5HuV) is upper bounded by $f(k)$
* [clique width]({{< base >}}html/wg5HuV) equal to $k$ implies that [boolean width]({{< base >}}html/A2jPWT) is upper bounded by $\mathcal O(k)$
* [boolean width]({{< base >}}html/A2jPWT) equal to $k$ implies that [clique width]({{< base >}}html/wg5HuV) is upper bounded by $2^{\mathcal O(k)}$
* [branch width]({{< base >}}html/lIcmuR) equal to $k$ implies that [boolean width]({{< base >}}html/A2jPWT) is upper bounded by $\mathcal O(k)$
* [branch width]({{< base >}}html/lIcmuR) equal to $k$ implies that [rank width]({{< base >}}html/fojquT) is upper bounded by $\mathcal O(k)$
* [treewidth]({{< base >}}html/5Q7fuR) equal to $k$ implies that [boolean width]({{< base >}}html/A2jPWT) is upper bounded by $f(k)$
* [bandwidth]({{< base >}}html/aP5a38) $k$ implies [cutwidth]({{< base >}}html/TLx1pz) is $k^{\mathcal O(1)}$ -- Any bandwidth bound cutwidth quadratically. An example where this happens is $(P_n)^k$ which has bandwidth $k$ and cutwidth $O(k^2)$; both seem to be optimal.
* [twin-cover number]({{< base >}}html/MUnHA0) equal to $k$ implies that [modular-width]({{< base >}}html/4bj71L) is upper bounded by $f(k)$
* bounded [modular-width]({{< base >}}html/4bj71L) does not imply bounded [twin-cover number]({{< base >}}html/MUnHA0)
* [neighborhood diversity]({{< base >}}html/vMs3RS) equal to $k$ implies that [modular-width]({{< base >}}html/4bj71L) is upper bounded by $f(k)$
* [modular-width]({{< base >}}html/4bj71L) equal to $k$ implies that [clique width]({{< base >}}html/wg5HuV) is upper bounded by $f(k)$
* [modular-width]({{< base >}}html/4bj71L) equal to $k$ implies that [diameter]({{< base >}}html/p4bTjp) is upper bounded by $f(k)$
* [neighborhood diversity]({{< base >}}html/vMs3RS) equal to $k$ implies that [boxicity]({{< base >}}html/a7MpiT) is upper bounded by $f(k)$
* [genus]({{< base >}}html/gbaHdw) equal to $k$ implies that [twin width]({{< base >}}html/MNTjuW) is upper bounded by $f(k)$
* [distance to planar]({{< base >}}html/distance_to_loZ5LD) equal to $k$ implies that [twin width]({{< base >}}html/MNTjuW) is upper bounded by $f(k)$
* [vertex integrity]({{< base >}}html/KVhJFB) is equal to [distance to bounded components]({{< base >}}html/distance_to_t7c4mp) -- By definition
* [bandwidth]({{< base >}}html/aP5a38) equal to $k$ implies that [topological bandwidth]({{< base >}}html/SnA7Eq) is upper bounded by $\mathcal O(k)$ -- By definition
* [twin-cover number]({{< base >}}html/MUnHA0) equal to $k$ implies that [distance to cluster]({{< base >}}html/distance_to_WAU7vf) is upper bounded by $\mathcal O(k)$ -- By definition
* [vertex cover]({{< base >}}html/4lp9Yj) equal to $k$ implies that [twin-cover number]({{< base >}}html/MUnHA0) is upper bounded by $\mathcal O(k)$ -- By definition
* [average degree]({{< base >}}html/z0y4TW) equal to $k$ implies that [minimum degree]({{< base >}}html/GPmOeT) is upper bounded by $\mathcal O(k)$ -- By definition
* [diameter]({{< base >}}html/p4bTjp) equal to $k$ implies that [average distance]({{< base >}}html/zH8PpT) is upper bounded by $\mathcal O(k)$ -- By definition
* [maximum matching]({{< base >}}html/veU7Jf) equal to $k$ implies that [maximum induced matching]({{< base >}}html/GzMYlT) is upper bounded by $\mathcal O(k)$ -- By definition
* [distance to interval]({{< base >}}html/distance_to_p5skoj) equal to $k$ implies that [boxicity]({{< base >}}html/a7MpiT) is upper bounded by $\mathcal O(k)$ -- By definition
* [bisection bandwidth]({{< base >}}html/wUdmUb) equal to $k$ implies that [edge connectivity]({{< base >}}html/JbqZoT) is upper bounded by $\mathcal O(k)$ -- By definition
* [vertex integrity]({{< base >}}html/KVhJFB) -- Minimum $k$ such that there exists $k$ vertices whose removal results in connected components of sizes at most $k$.
* [twin-cover number]({{< base >}}html/MUnHA0) -- Distance to cluster where all vertices of each clique are siblings.
* [maximum degree]({{< base >}}html/UyQ5yM) -- maximum degree of graph's vertices
* [feedback vertex set]({{< base >}}html/GNOiyB) -- can be thought of as a *distance to forest*
* [minimum degree]({{< base >}}html/GPmOeT) -- minimum degree of graph's vertices
* [treedepth]({{< base >}}html/KEP2qM) equal to $k$ implies that [diameter]({{< base >}}html/p4bTjp) is upper bounded by $f(k)$ -- An unbounded diameter implies the class contains paths as subgraphs. Minimum treedepth to embed a path of length $n$ in a treedepth tree is $\log n$.
* [feedback vertex set]({{< base >}}html/GNOiyB) is equal to [distance to forest]({{< base >}}html/distance_to_JngPPm)
* [vertex cover]({{< base >}}html/4lp9Yj) is equal to [distance to edgeless]({{< base >}}html/distance_to_LsiBbX)
* [odd cycle transversal]({{< base >}}html/Ve5ruW) is equal to [distance to bipartite]({{< base >}}html/distance_to_cLHJkW) -- Bipartite graphs is the graph class without any odd cycles.
* bounded [complete]({{< base >}}html/EhdXNA) does not imply bounded [maximum clique]({{< base >}}html/q7zHeT) -- Parameter is unbounded for the graph class of cliques.
* bounded [complete]({{< base >}}html/EhdXNA) does not imply bounded [domatic number]({{< base >}}html/KRV6tI) -- Parameter is unbounded for the graph class of cliques.
* bounded [complete]({{< base >}}html/EhdXNA) does not imply bounded [edge connectivity]({{< base >}}html/JbqZoT) -- Parameter is unbounded for the graph class of cliques.
* bounded [co-cluster]({{< base >}}html/7HR4uV) does not imply bounded [distance to chordal]({{< base >}}html/distance_to_Cv1PaJ)
* the [cluster]({{< base >}}html/WAU7vf) class has bounded [twin-cover number]({{< base >}}html/MUnHA0) by a constant
* bounded [cluster]({{< base >}}html/WAU7vf) does not imply bounded [domination number]({{< base >}}html/Gq0onN)
* bounded [bipartite]({{< base >}}html/cLHJkW) does not imply bounded [girth]({{< base >}}html/BCwUeT)
* bounded [bipartite]({{< base >}}html/cLHJkW) does not imply bounded [edge connectivity]({{< base >}}html/JbqZoT)
* the [forest]({{< base >}}html/JngPPm) class has bounded [feedback edge set]({{< base >}}html/HTk9PZ) by a constant
* bounded [forest]({{< base >}}html/JngPPm) does not imply bounded [girth]({{< base >}}html/BCwUeT)
* bounded [forest]({{< base >}}html/JngPPm) does not imply bounded [pathwidth]({{< base >}}html/VHClqR)
* bounded [forest]({{< base >}}html/JngPPm) does not imply bounded [distance to interval]({{< base >}}html/distance_to_p5skoj)
* the [edgeless]({{< base >}}html/LsiBbX) class has bounded [vertex cover]({{< base >}}html/4lp9Yj) by a constant
* bounded [edgeless]({{< base >}}html/LsiBbX) does not imply bounded [domination number]({{< base >}}html/Gq0onN)
* bounded [grid]({{< base >}}html/lfYXuK) does not imply bounded [clique width]({{< base >}}html/wg5HuV)
* bounded [grid]({{< base >}}html/lfYXuK) does not imply bounded [distance to chordal]({{< base >}}html/distance_to_Cv1PaJ)
* bounded [grid]({{< base >}}html/lfYXuK) does not imply bounded [average distance]({{< base >}}html/zH8PpT)
* bounded [grid]({{< base >}}html/lfYXuK) does not imply bounded [bisection bandwidth]({{< base >}}html/wUdmUb)
* the [disjoint cycles]({{< base >}}html/AGnF5Z) class has bounded [bisection bandwidth]({{< base >}}html/wUdmUb) by a constant
* the [outerplanar]({{< base >}}html/0oCyaG) class has bounded [bisection bandwidth]({{< base >}}html/wUdmUb) by a constant
* the [grid]({{< base >}}html/lfYXuK) class has bounded [maximum degree]({{< base >}}html/UyQ5yM) by a constant
* bounded [disjoint cycles]({{< base >}}html/AGnF5Z) does not imply bounded [girth]({{< base >}}html/BCwUeT)
* bounded [interval]({{< base >}}html/p5skoj) does not imply bounded [average distance]({{< base >}}html/zH8PpT)
* bounded [path]({{< base >}}html/ryPlqz) does not imply bounded [treedepth]({{< base >}}html/KEP2qM)
* bounded [linear forest]({{< base >}}html/skQuFN) does not imply bounded [average distance]({{< base >}}html/zH8PpT)
* the [planar]({{< base >}}html/loZ5LD) class has bounded [genus]({{< base >}}html/gbaHdw) by a constant
* bounded [planar]({{< base >}}html/loZ5LD) does not imply bounded [girth]({{< base >}}html/BCwUeT)
* bounded [planar]({{< base >}}html/loZ5LD) does not imply bounded [maximum degree]({{< base >}}html/UyQ5yM)
* bounded [planar]({{< base >}}html/loZ5LD) does not imply bounded [distance to perfect]({{< base >}}html/distance_to_RmssrZ)
* the [constant components]({{< base >}}html/FJ8gmU) class has bounded [cutwidth]({{< base >}}html/TLx1pz) by a constant
* bounded [constant components]({{< base >}}html/FJ8gmU) does not imply bounded [distance to perfect]({{< base >}}html/distance_to_RmssrZ)
* bounded [constant components]({{< base >}}html/FJ8gmU) does not imply bounded [distance to planar]({{< base >}}html/distance_to_loZ5LD)
* bounded [stars]({{< base >}}html/10JR3F) does not imply bounded [h-index]({{< base >}}html/GNTwUS)
* bounded [stars]({{< base >}}html/10JR3F) does not imply bounded [vertex integrity]({{< base >}}html/KVhJFB)
* bounded [disjoint cycles]({{< base >}}html/AGnF5Z) does not imply bounded [distance to perfect]({{< base >}}html/distance_to_RmssrZ)
* the [cycle]({{< base >}}html/Ti0asF) class has bounded [maximum leaf number]({{< base >}}html/BN92vX) by a constant
* bounded [cycle]({{< base >}}html/Ti0asF) does not imply bounded [girth]({{< base >}}html/BCwUeT)