

# strongly connected components are paritions of a directed graph
# such that every pair of vertices (u, v) within a parition are reachable from each other (ie. u->v and v->u)



# there are two major algorithms for deciding such paritions
# 1. 
# 2. Tarjan's SCC algorithm by Robert Tarjan



def tarjan_scc(adj_list: dict[str, list[str]]) -> list[list[str]]:
    
    low_link_map = dict()       # tracks the lowest discover time of nodes that current node can reach
    partitions = []
    stack = []
    on_stack_elem = set()

    def dfs(node: str):
        stack.append(node)
        on_stack_elem.add(node)
        discover_time = len(low_link_map)
        low_link_map[node] = discover_time

        for neighbor in adj_list[node]:
            if not neighbor in  low_link_map:   # not yet visited
                dfs(neighbor)
                low_link_map[node] = min(low_link_map[node], low_link_map[neighbor])
            
            # spotted a backedge
            elif neighbor in on_stack_elem: 
                low_link_map[node] = min(low_link_map[node], low_link_map[neighbor])

        # current node started the scc
        if low_link_map[node] == discover_time:
            partition = []
            while len(stack):
                val = stack.pop()
                partition.append(val)
                on_stack_elem.remove(val)
                if val == node:
                    break
            partitions.append(partition)

    # dfs all nodes not yet discovered
    for node in adj_list.keys():
        if node in low_link_map:
            continue
        dfs(node)
    
    return partitions

        


adj1 = {
    "A" : ["B"],
    "B" : ["C"],
    "C" : ["A"]
}

adj2 = {
    "A" : ["B"],
    "B" : ["C"],
    "C" : ["A"],
    "D" : ["E"],
    "E" : []
}


adj3 = {
    "A" : ["B"],
    "B" : ["C", "D"],
    "C" : ["A"],
    "D" : ["E"],
    "E" : ["F"],
    "F" : ["D"]
}

adj4 = {
        "A": ["B"],
        "B": ["C", "F", "E"],
        "C": ["D", "G"],
        "D": ["C", "H"],
        "E": ["A", "F"],
        "F": ["G", "I"],
        "G": ["F", "J"],
        "H": ["D", "K"],
        "I": ["J"],
        "J": ["I"],
        "K": ["H", "J"]
    }


def pretty_print(partitions):
    for p in partitions:
        p.sort()
    partitions.sort()
    print(partitions)



pretty_print(tarjan_scc(adj1))
pretty_print(tarjan_scc(adj2))
pretty_print(tarjan_scc(adj3))
pretty_print(tarjan_scc(adj4))









