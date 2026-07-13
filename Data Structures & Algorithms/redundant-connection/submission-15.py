class DSU:
    def __init__(self, n):
        self.forests = n + 1
        self.parent = list(range(self.forests + 1))
        self.rank = [1] * (self.forests + 1)

    def find(self, u):
        p = u

        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        
        return p
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)

        if pu == pv:
            return True
        
        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pv] < self.rank[pu]:
            self.parent[pv] = pu
        else:
            self.parent[pu] = pv
            self.rank[pv] += 1
        
        return False

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        dsu = DSU(n)

        for u,v in edges:
            if dsu.union(u,v):
                return [u, v]
            
        return []
        

