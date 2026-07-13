class DSU:
    def __init__(self, n):
        self.n = n
        
        self.parent = {}
        self.rank = {}

        for i in range(self.n + 1):
            self.parent[i] = i
            self.rank[i] = 1
    
    def find(self, vertex):
        v = vertex

        while v != self.parent[v]:
            self.parent[v] = self.parent[self.parent[v]]
            v = self.parent[v]
        
        return v
    
    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)

        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        if self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1
        
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)

        dsu = DSU(N)

        for u, v in (edges):
            if not dsu.union(u,v):
                return [u,v]
        