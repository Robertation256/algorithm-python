from collections import deque


# time complexity: O(V+E)
# space complexity: O(V)


def bfs(start_node:str, adj_list: dict[str: list[str]]):
    visited = set()
    q = deque()
    q.append(start_node)
    visited.add(start_node)

    while len(q):
        for _ in range(len(q)):  #range obj stores integer thus fixes to length on init
            cur = q.popleft()
            # do something with current node
            for neighbor in adj_list[cur]:
                if neighbor in visited:
                    continue
                q.append(neighbor)
                visited.add(neighbor)




    
