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
def shortest_pathes(dist: dict[int, dict[int, int]], vertices_count: int):
    min_cost = [[float('inf') for i in range(vertices_count)] for j in range(vertices_count)]

    for u in dist.keys():
        for v in dist[u].keys():
            min_cost[u][v] = min(min_cost[u][v], dist[u][v])
    

    for u in range(vertices_count):
        for v in range(vertices_count):
            if u == v:
                min_cost[u][v] = 0
                continue
            for k in range(vertices_count): # k the intermediary vertices that we wish to connect u and v
                min_cost[u][v] = min(min_cost[u][v], min_cost[u][k] + min_cost[k][v])
    return min_cost



