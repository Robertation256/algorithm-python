from collections import deque


# time complexity: O(V+E)
# space complexity: O(V)


def bfs(start_node:str, adj_list: dict[str: list[str]]):
    in_queue = set()
    q = deque()
    q.append(start_node)
    in_queue.add(start_node)

    while len(q):
        for _ in range(len(q)):  #range obj stores integer thus fixes to length on init
            cur = q.popleft()
            # do something with current node
            for neighbor in adj_list[cur]:
                if neighbor in in_queue:
                    continue
                q.append(neighbor)
                in_queue.add(neighbor)




    
