class DSU:
    def __init__(self,size):
        self.parent = {}
        self.rank = {}

        for i in range(size):
            self.parent[i] = i
            self.rank[i] = 1
    
    def find(self, vertex):
        root = vertex

        while root != self.parent[root]:
            self.parent[root] = self.parent[self.parent[root]]
            root = self.parent[root]
        
        return root

    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)

        if p1 == p2:
            return 0
        
        if self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        elif self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1
        
        return 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        componentCount = n
        dsu = DSU(n)

        for u,v in edges:
            componentCount -= dsu.union(u,v)
        
        return componentCount