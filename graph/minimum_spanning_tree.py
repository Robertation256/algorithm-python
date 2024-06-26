

# given an undirected, connected graph with weighted edges, 
# find a set of edges that connect all vertices whose total weight is minimized
# since this set of edge is acyclic and connects all vertices, it must form a tree
# aka. the minimum spanning tree

# MST comes in two implementation flavors
# 1. Kruskal’s algorithm (union-find based)
# 2. Prims's algorithm  (priority queue based)



# assume input of a list edges(u, v ,weight)

#time complexity: O(ElogE + ElogV) since E <= V**2, ElogE == ElogV, complexity is ElogE
#space complexity: O(V)
def kruskal_mst(edges: list[tuple[str, str, int]]):

    # setup union-find
    parent = dict()
    for u, v, _ in edges:
        parent[u] = u
        parent[v] = v

    def find(a):
        if a != parent[a]:
            return find(parent[a])
        return a

    def union(a, b):
        parent[find(b)] = find(a)

    # sort by weight
    edges.sort(key=lambda x: x[2])  

    cost = 0

    for u, v, weight in edges:
        if find(u) != find(v):
            union(u, v)
            cost += weight 
    
    return cost


    

