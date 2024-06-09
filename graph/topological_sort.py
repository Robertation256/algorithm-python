
# produce a linear ordering of vertices such that for every directed edge u-v, vertex u comes before v in the ordering.
# used for resolving dependency and cycle detection in a directed graph
def topological_sort(nodes: list[str], adj_list: dict[str, list[str]]):
    in_degree = {n: 0 for n in nodes}
    candidates = []
    res = []
    for vs in adj_list.values():
        for v in vs:
            in_degree[v] += 1

    for n in nodes:
        if in_degree[n] == 0:
            candidates.append(n)

    while len(candidates):
        node = candidates.pop()
        res.append(node)
        for neighbor in adj_list[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                candidates.append(neighbor)
    return res
    



