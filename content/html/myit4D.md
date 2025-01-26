# unknown source

This knowledge was added to the database without tying it to an appropriate resource.

* [linear forest]({{< base >}}html/skQuFN) -- Disjoint union of paths.
* [maximum matching on bipartite graphs]({{< base >}}html/8Mm5qJ) upper and lower bounds [vertex cover]({{< base >}}html/4lp9Yj) by a linear function -- Kőnig's theorem
* [vertex cover]({{< base >}}html/4lp9Yj) upper and lower bounds [maximum matching]({{< base >}}html/veU7Jf) by a linear function -- Every edge of the matching needs to be covered by at least one vertex. Path shows lower bound.
* [odd cycle transversal]({{< base >}}html/Ve5ruW) is equivalent to [distance to bipartite]({{< base >}}html/1yW82F) -- Bipartite graphs is the graph class without any odd cycles.
* [distance to bipartite]({{< base >}}html/1yW82F) is equivalent to [odd cycle transversal]({{< base >}}html/Ve5ruW) -- Bipartite graphs is the graph class without any odd cycles.
* [feedback edge set]({{< base >}}html/HTk9PZ) upper bounds [feedback vertex set]({{< base >}}html/GNOiyB) by a linear function -- Given solution to feedback edge set one can remove one vertex incident to the solution edges to obtain feedback vertex set.
* [feedback edge set]({{< base >}}html/HTk9PZ) upper bounds [genus]({{< base >}}html/gbaHdw) by a linear function -- Removing $k$ edges creates a forest that is embeddable into the plane. We now add one handle for each of the $k$ edges to get embedding into $k$-handle genus.
* [chromatic number]({{< base >}}html/w7MmyW) upper bounds [maximum clique]({{< base >}}html/q7zHeT) by a linear function -- Unbounded clique implies the number of needed colors is unbounded.
* [degeneracy]({{< base >}}html/VowkuW) upper bounds [chromatic number]({{< base >}}html/w7MmyW) by a linear function -- Greedily color the vertices in order of the degeneracy ordering. As each vertex has at most $k$ colored predecesors we use at most $k+1$ colors.
* [degeneracy]({{< base >}}html/VowkuW) upper bounds [average degree]({{< base >}}html/z0y4TW) by a linear function -- Removing a vertex of degree $d$ increases the value added to the sum of all degrees by at most $2d$, hence, the average is no more than twice the degeneracy.
* [maximum degree]({{< base >}}html/UyQ5yM) upper bounds [h-index]({{< base >}}html/GNTwUS) by a linear function -- As h-index seeks $k$ vertices of degree $k$ it is trivially upper bound by maximum degree.
* [minimum degree]({{< base >}}html/GPmOeT) upper bounds [edge connectivity]({{< base >}}html/JbqZoT) by a linear function -- Removing edges incident to the minimum degree vertex disconnects the graph.
* [linear rank-width]({{< base >}}html/cHugsk) upper bounds [rank-width]({{< base >}}html/fojquT) by a computable function
* [pathwidth]({{< base >}}html/VHClqR) upper bounds [linear rank-width]({{< base >}}html/cHugsk) by a computable function
* [minimum degree]({{< base >}}html/GPmOeT) upper bounds [domatic number]({{< base >}}html/KRV6tI) by a linear function -- The vertex of minimum degree needs to be dominated in each of the sets. As the sets cannot overlap there can be at most $k+1$ of them.
* [distance to linear forest]({{< base >}}html/yk7XP0) upper bounds [pathwidth]({{< base >}}html/VHClqR) by a linear function -- After removal of $k$ vertices the remaining class has a bounded width $w$. So by including the removed vertices in every bag, we can achieve decomposition of width $w+k$
* [topological bandwidth]({{< base >}}html/SnA7Eq) upper bounds [bisection bandwidth]({{< base >}}html/wUdmUb) by a linear function -- Order vertices by their bandwidth integer. We split the graph in the middle of this ordering. There are at most roughly $k^2/2$ edges over this split.
* [bandwidth]({{< base >}}html/aP5a38) upper bounds [maximum degree]({{< base >}}html/UyQ5yM) by a linear function -- Each vertex has an integer $i$ and may be connected only to vertices whose difference from $i$ is at most $k$. There are at most $k$ bigger and $k$ smaller such neighbors.
* [distance to linear forest]({{< base >}}html/yk7XP0) upper bounds [pathwidth]({{< base >}}html/VHClqR) by a linear function -- After removal of $k$ vertices the remaining class has a bounded width $w$. So by including the removed vertices in every bag, we can achieve decomposition of width $w+k$
* [distance to outerplanar]({{< base >}}html/lPHVWU) upper bounds [treewidth]({{< base >}}html/5Q7fuR) by a linear function -- After removal of $k$ vertices the remaining class has a bounded width $w$. So by including the removed vertices in every bag, we can achieve decomposition of width $w+k$
* [vertex integrity]({{< base >}}html/KVhJFB) upper bounds [treedepth]({{< base >}}html/KEP2qM) by a linear function -- First, treedepth removes vertices of the modulator, then it iterates through remaining components one by one.
* [distance to stars]({{< base >}}html/Z10jME) upper bounds [treedepth]({{< base >}}html/KEP2qM) by a linear function -- First, treedepth removes vertices of the modulator, remainder has treedepth $2$
* [distance to complete]({{< base >}}html/2LDMQ6) upper bounds [clique cover number]({{< base >}}html/VomShB) by a linear function -- We cover the $k$ vertices of the modulator by cliques of size $1$ and cover the remaining clique by another one.
* [maximum independent set]({{< base >}}html/mHtXUU) upper bounds [domination number]({{< base >}}html/Gq0onN) by a linear function -- Every maximal independent set is also a dominating set because any undominated vertex could be added to the independent set.
* [domination number]({{< base >}}html/Gq0onN) upper bounds [diameter]({{< base >}}html/p4bTjp) by a linear function -- An unbounded diameter implies a long path where no vertices that are more than $3$ apart may be dominated by the same dominating vertex, otherwise we could shorten the path. Hence, the number of dominating vertices is also unbounded.
* [distance to bipartite]({{< base >}}html/1yW82F) upper bounds [chromatic number]({{< base >}}html/w7MmyW) by a linear function -- Removed vertices get one color each and we need only $2$ colors for the rest.
* [edge clique cover number]({{< base >}}html/nYQDv6) upper bounds [neighborhood diversity]({{< base >}}html/vMs3RS) by an exponential function -- Label vertices by the cliques they are contained in, each label is its own group in the neighborhood diversity, connect accordingly.
* [distance to complete]({{< base >}}html/2LDMQ6) upper bounds [edge clique cover number]({{< base >}}html/nYQDv6) by a polynomial function -- Cover the remaining clique, cover each modulator vertex and its neighborhood outside of it with another clique, cover each edge within the modulator by its own edge.
* [treewidth]({{< base >}}html/5Q7fuR) upper bounds [book thickness]({{< base >}}html/doijTS) by a computable function
* [maximum leaf number]({{< base >}}html/BN92vX) upper bounds [distance to linear forest]({{< base >}}html/yk7XP0) by a computable function
* [acyclic chromatic number]({{< base >}}html/QGZuUW) upper bounds [boxicity]({{< base >}}html/a7MpiT) by a computable function
* [h-index]({{< base >}}html/GNTwUS) upper bounds [distance to maximum degree]({{< base >}}html/kRR8zx) by a linear function -- Remove the $h$ vertices of degree at least $h$ to get a graph that has maximum degree $h$.
* [distance to maximum degree]({{< base >}}html/kRR8zx) upper bounds [h-index]({{< base >}}html/GNTwUS) by a linear function -- Removal of $k$ vertices yielding a graph with maximum degree $c$ means that there were $k$ vertices of arbitrary degree and the remaining vertices had degree at most $k+c$. Hence, $h$-index is no more than $k+c$.
* [distance to cograph]({{< base >}}html/uDXX2i) upper bounds [chordality]({{< base >}}html/fTqo40) by a linear function
* [distance to cograph]({{< base >}}html/uDXX2i) upper bounds [diameter]({{< base >}}html/p4bTjp) by a linear function
* [book thickness]({{< base >}}html/doijTS) upper bounds [acyclic chromatic number]({{< base >}}html/QGZuUW) by a computable function
* [average distance]({{< base >}}html/zH8PpT) upper bounds [girth]({{< base >}}html/BCwUeT) by a computable function
* [maximum leaf number]({{< base >}}html/BN92vX) upper bounds [feedback edge set]({{< base >}}html/HTk9PZ) by a computable function
* [maximum induced matching]({{< base >}}html/GzMYlT) upper bounds [diameter]({{< base >}}html/p4bTjp) by a linear function -- Diameter requires an induced path on $d$ edges, hence, maximum induced matching is at least $\lfloor (d+1)/3 \rfloor$.
* [maximum independent set]({{< base >}}html/mHtXUU) upper bounds [maximum induced matching]({{< base >}}html/GzMYlT) by a linear function -- Each edge of the induced matching can host at one vertex of the independent set.
* [vertex cover]({{< base >}}html/4lp9Yj) upper bounds [neighborhood diversity]({{< base >}}html/vMs3RS) by an exponential function
* bounded [twin-cover number]({{< base >}}html/MUnHA0) does not imply bounded [neighborhood diversity]({{< base >}}html/vMs3RS)
* [linear clique-width]({{< base >}}html/fQj3wU) upper bounds [clique-width]({{< base >}}html/wg5HuV) by a computable function
* [clique-width]({{< base >}}html/wg5HuV) upper bounds [boolean width]({{< base >}}html/A2jPWT) by a linear function
* [boolean width]({{< base >}}html/A2jPWT) upper bounds [clique-width]({{< base >}}html/wg5HuV) by an exponential function
* [branch width]({{< base >}}html/lIcmuR) upper bounds [boolean width]({{< base >}}html/A2jPWT) by a linear function
* [module-width]({{< base >}}html/EV3FqL) upper bounds [clique-width]({{< base >}}html/wg5HuV) by a computable function
* [clique-width]({{< base >}}html/wg5HuV) upper bounds [module-width]({{< base >}}html/EV3FqL) by a computable function
* [treewidth]({{< base >}}html/5Q7fuR) upper bounds [mm-width]({{< base >}}html/d7vRYU) by a computable function
* [mm-width]({{< base >}}html/d7vRYU) upper bounds [treewidth]({{< base >}}html/5Q7fuR) by a computable function
* [branch width]({{< base >}}html/lIcmuR) upper bounds [rank-width]({{< base >}}html/fojquT) by a linear function
* [treewidth]({{< base >}}html/5Q7fuR) upper bounds [boolean width]({{< base >}}html/A2jPWT) by a computable function
* [bandwidth]({{< base >}}html/aP5a38) upper and lower bounds [cutwidth]({{< base >}}html/TLx1pz) by a polynomial function -- Any bandwidth bound cutwidth quadratically. An example where this happens is $(P_n)^k$ which has bandwidth $k$ and cutwidth $O(k^2)$; both seem to be optimal.
* [modular-width]({{< base >}}html/4bj71L) upper bounds [clique-width]({{< base >}}html/wg5HuV) by a computable function
* [modular-width]({{< base >}}html/4bj71L) upper bounds [diameter]({{< base >}}html/p4bTjp) by a computable function
* [maximum degree]({{< base >}}html/UyQ5yM) upper bounds [c-closure]({{< base >}}html/ou9VU1) by a computable function
* [feedback edge set]({{< base >}}html/HTk9PZ) upper bounds [c-closure]({{< base >}}html/ou9VU1) by a computable function
* [vertex integrity]({{< base >}}html/KVhJFB) -- Minimum $k$ such that there exists $k$ vertices whose removal results in connected components of sizes at most $k$.
* [twin-cover number]({{< base >}}html/MUnHA0) -- Distance to cluster where all vertices of each clique are siblings.
* [maximum degree]({{< base >}}html/UyQ5yM) -- maximum degree of graph's vertices
* [feedback vertex set]({{< base >}}html/GNOiyB) -- can be thought of as a *distance to forest*
* [minimum degree]({{< base >}}html/GPmOeT) -- minimum degree of graph's vertices
* [diameter]({{< base >}}html/p4bTjp) -- Maximum distance of two vertices that are in the same connected component.
* [feedback vertex set]({{< base >}}html/GNOiyB) is equivalent to [distance to forest]({{< base >}}html/hQZlLU)
* [distance to forest]({{< base >}}html/hQZlLU) is equivalent to [feedback vertex set]({{< base >}}html/GNOiyB)
* [vertex cover]({{< base >}}html/4lp9Yj) is equivalent to [distance to edgeless]({{< base >}}html/4INs10)
* [distance to edgeless]({{< base >}}html/4INs10) is equivalent to [vertex cover]({{< base >}}html/4lp9Yj)
* graph class [complete]({{< base >}}html/EhdXNA) has unbounded [maximum clique]({{< base >}}html/q7zHeT) -- Parameter is unbounded for the graph class of cliques.
* graph class [complete]({{< base >}}html/EhdXNA) has unbounded [domatic number]({{< base >}}html/KRV6tI) -- Parameter is unbounded for the graph class of cliques.
* graph class [complete]({{< base >}}html/EhdXNA) has unbounded [edge connectivity]({{< base >}}html/JbqZoT) -- Parameter is unbounded for the graph class of cliques.
* graph class [co-cluster]({{< base >}}html/7HR4uV) has unbounded [distance to chordal]({{< base >}}html/OdZQna)
* graph class [cluster]({{< base >}}html/WAU7vf) has constant [twin-cover number]({{< base >}}html/MUnHA0)
* graph class [cluster]({{< base >}}html/WAU7vf) has unbounded [domination number]({{< base >}}html/Gq0onN)
* graph class [bipartite]({{< base >}}html/cLHJkW) has unbounded [girth]({{< base >}}html/BCwUeT)
* graph class [bipartite]({{< base >}}html/cLHJkW) has unbounded [edge connectivity]({{< base >}}html/JbqZoT)
* graph class [forest]({{< base >}}html/JngPPm) has constant [feedback edge set]({{< base >}}html/HTk9PZ)
* graph class [forest]({{< base >}}html/JngPPm) has unbounded [girth]({{< base >}}html/BCwUeT)
* graph class [forest]({{< base >}}html/JngPPm) has unbounded [distance to interval]({{< base >}}html/AVc2K6)
* graph class [edgeless]({{< base >}}html/LsiBbX) has constant [vertex cover]({{< base >}}html/4lp9Yj)
* graph class [edgeless]({{< base >}}html/LsiBbX) has unbounded [domination number]({{< base >}}html/Gq0onN)
* graph class [grid]({{< base >}}html/lfYXuK) has unbounded [distance to chordal]({{< base >}}html/OdZQna)
* graph class [grid]({{< base >}}html/lfYXuK) has unbounded [average distance]({{< base >}}html/zH8PpT)
* graph class [grid]({{< base >}}html/lfYXuK) has unbounded [bisection bandwidth]({{< base >}}html/wUdmUb)
* graph class [disjoint cycles]({{< base >}}html/AGnF5Z) has constant [bisection bandwidth]({{< base >}}html/wUdmUb)
* graph class [outerplanar]({{< base >}}html/0oCyaG) has constant [bisection bandwidth]({{< base >}}html/wUdmUb)
* graph class [grid]({{< base >}}html/lfYXuK) has constant [maximum degree]({{< base >}}html/UyQ5yM)
* graph class [disjoint cycles]({{< base >}}html/AGnF5Z) has unbounded [girth]({{< base >}}html/BCwUeT)
* graph class [interval]({{< base >}}html/p5skoj) has unbounded [average distance]({{< base >}}html/zH8PpT)
* graph class [path]({{< base >}}html/ryPlqz) has unbounded [treedepth]({{< base >}}html/KEP2qM)
* graph class [linear forest]({{< base >}}html/skQuFN) has unbounded [average distance]({{< base >}}html/zH8PpT)
* graph class [planar]({{< base >}}html/loZ5LD) has constant [genus]({{< base >}}html/gbaHdw)
* graph class [planar]({{< base >}}html/loZ5LD) has unbounded [girth]({{< base >}}html/BCwUeT)
* graph class [planar]({{< base >}}html/loZ5LD) has unbounded [maximum degree]({{< base >}}html/UyQ5yM)
* graph class [planar]({{< base >}}html/loZ5LD) has unbounded [distance to perfect]({{< base >}}html/kJZKgd)
* bounded [vertex integrity]({{< base >}}html/KVhJFB) does not imply bounded [neighborhood diversity]({{< base >}}html/vMs3RS)
* graph class [stars]({{< base >}}html/10JR3F) has unbounded [h-index]({{< base >}}html/GNTwUS)
* graph class [stars]({{< base >}}html/10JR3F) has unbounded [vertex integrity]({{< base >}}html/KVhJFB)
* graph class [cycles]({{< base >}}html/2iJr52) has unbounded [distance to perfect]({{< base >}}html/kJZKgd)
* graph class [cycle]({{< base >}}html/Ti0asF) has constant [maximum leaf number]({{< base >}}html/BN92vX)
* graph class [cycle]({{< base >}}html/Ti0asF) has unbounded [girth]({{< base >}}html/BCwUeT)
* [maximum leaf number]({{< base >}}html/BN92vX) upper bounds [feedback edge set]({{< base >}}html/HTk9PZ) by a polynomial function -- M. Bentert (personal communication)
* [bounded components]({{< base >}}html/t7c4mp) upper bounds [cutwidth]({{< base >}}html/TLx1pz) by a polynomial function -- By greedily placing one component after another.
* bounded [bounded components]({{< base >}}html/t7c4mp) does not imply bounded [distance to perfect]({{< base >}}html/kJZKgd) -- By a disjoint union of small components with distance to perfect at least 1.
* bounded [bounded components]({{< base >}}html/t7c4mp) does not imply bounded [distance to planar]({{< base >}}html/MLJMRH) -- By a disjoint union of many $K_5$ graphs.
* graph class [star]({{< base >}}html/CortlU) has constant [vertex cover]({{< base >}}html/4lp9Yj) -- trivially
* graph class [star]({{< base >}}html/CortlU) has constant [h-index]({{< base >}}html/GNTwUS) -- trivially
* graph class [tree]({{< base >}}html/rJyICu) has unbounded [h-index]({{< base >}}html/GNTwUS) -- trivially
* graph class [path]({{< base >}}html/ryPlqz) has unbounded [distance to cluster]({{< base >}}html/aXw3Co) -- trivially
* graph class [path]({{< base >}}html/ryPlqz) has unbounded [diameter]({{< base >}}html/p4bTjp) -- trivially
* graph class [cycles]({{< base >}}html/2iJr52) has constant [pathwidth]({{< base >}}html/VHClqR) -- trivially
* graph class [star]({{< base >}}html/CortlU) has unbounded [maximum degree]({{< base >}}html/UyQ5yM) -- trivially
* graph class [complete]({{< base >}}html/EhdXNA) has unbounded [maximum matching]({{< base >}}html/veU7Jf)
* graph class [path]({{< base >}}html/ryPlqz) has unbounded [maximum matching]({{< base >}}html/veU7Jf)
* graph class [star]({{< base >}}html/CortlU) has constant [maximum matching]({{< base >}}html/veU7Jf)
* graph class [edgeless]({{< base >}}html/LsiBbX) has constant [maximum matching]({{< base >}}html/veU7Jf)
* [clique-width]({{< base >}}html/wg5HuV) upper bounds [mim-width]({{< base >}}html/WmIFB1) by a computable function
* [mim-width]({{< base >}}html/WmIFB1) upper bounds [sim-width]({{< base >}}html/aEGv5N) by a computable function
* [treewidth]({{< base >}}html/5Q7fuR) upper bounds [tree-independence number]({{< base >}}html/fNR6QK) by a computable function
* [tree-independence number]({{< base >}}html/fNR6QK) upper bounds [sim-width]({{< base >}}html/aEGv5N) by a computable function
* [clique-width]({{< base >}}html/wg5HuV) upper bounds [twin-width]({{< base >}}html/OrH7et) by a computable function