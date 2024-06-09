

# complexity: same as bfs
def dfs(start_node: str, adj_list: dict[str, list[str]], visited = set()):
    visited.add(start_node)
    # do something with current node
    for neighbor in adj_list[start_node]:
        if neighbor not in visited: 
            dfs(neighbor, adj_list, visited)

    