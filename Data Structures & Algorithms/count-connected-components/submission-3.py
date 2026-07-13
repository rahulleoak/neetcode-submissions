class DSU:
    def __init__(self, n):
        self.forests = n
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, u):
        p = u

        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]

        return p
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)

        if pu == pv:
            return
        
        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pv] < self.rank[pu]:
            self.parent[pv] = pu
        else:
            self.parent[pu] = pv
            self.rank[pv] += 1
        
        self.forests -= 1
    
    def forestCount(self):
        return self.forests

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)

        for u,v in edges:
            dsu.union(u,v)
        
        return dsu.forestCount()

        