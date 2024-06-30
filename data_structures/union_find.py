

class UnionFind():

    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.tree_height = [0 for i in range(size)] # track the height of the tree rooting at i
        self.tree_count = size      # number of trees 


    def find(self, node):
        while self.parent[node] != node:
            node = self.parent[node]
        return node 

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)

        if u == v:
            return 

        # join shorter tree to higher tree for optimized max depth
        if self.tree_height[u] >= self.tree_height[v]:
            self.tree_height[u] = max(self.tree_height[u], self.tree_height[v] + 1)
            self.parent[v] = u  
        else:
            self.parent[u] = v  

        self.tree_count -= 1 

    def is_connected(self):
        return self.tree_count == 1
