from heapq import heapify, heappush, heappop



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

