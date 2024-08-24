from heapq import heapify, heappush, heappop


# time complexity O((V+E)logV)
# space complexity O(V) (ie when one node is connected to the rest of the nodes)
def dijkstra_shortest_path(adj_list: dict[str, list[tuple[str, int]]], start_node: str):
    
    dst_from_start = {n: float('inf') for n in adj_list.keys()}
    dst_from_start[start_node] = 0

    prev_node = {n: n for n in adj_list.keys()}

    heap = [(0, start_node)]


    while len(heap):
        dst, node = heappop(heap)
        for neighbor, weight in adj_list[node]:
            new_dst = weight + dst
            if new_dst < dst_from_start[neighbor]:
                heappush((new_dst, neighbor))
                dst_from_start[neighbor] = new_dst
                prev[neighbor] = node 

    return dst_from_start, prev_node


# Floyd–Warshall algorithm
# for computing shortest paths between all pairs of vertices in a directed, weighted graph
# complexity O(V^3)
# let f(i, j, k) denote the shortest path we can get from node i to j using first k nodes as intermediate nodes
# f(i, j, 0) is thus the minimum edge weight from i to j
# f(i, j, k) = min(f(i, k, k-1) + f(k, j, k-1), f(i, j, k-1)) since we can either use or not use the k-th node as intermediary node
def shortest_pathes(dist: dict[tuple[int, int], int], vertices_count: int):
    distance_matrix = [[float('inf') for i in range(vertices_count)] for j in range(vertices_count)]

    for u in range(vertices_count):
        for v in range(vertices_count):
            if (u, v) in dist:
                distance_matrix[u][v] = min(distance_matrix[u][v], dist[(u, v)])
    

    for k in range(vertices_count):
        for u in range(vertices_count):
            for v in range(vertices_count):
                distance_matrix[u][v] = min(
                    distance_matrix[u][v],
                    # note that we update the previous matrix snapshot representing f(*, *, k-1) in place here
                    distance_matrix[u][k] + distance_matrix[k][v]
                )
    return distance_matrix





