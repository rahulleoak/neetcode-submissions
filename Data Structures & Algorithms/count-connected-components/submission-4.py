class DSU:
    def __init__(self, n):
        self.n = n
        self.parents = list(range(n))
        self.rank = [1] * n
    
    def find(self, u):
        p = u

        while self.parents[p] != p:
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]
        
        return p
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)

        if pu == pv:
            return 
        
        if self.rank[pu] < self.rank[pv]:
            self.parents[pu] = pv
        elif self.rank[pv] < self.rank[pu]:
            self.parents[pv] = pu
        else:
            self.parents[pv] = pu
            self.rank[pu] += 1

        self.n -= 1
        return

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)

        for u,v in edges:
            dsu.union(u,v)
        
        return dsu.n
        