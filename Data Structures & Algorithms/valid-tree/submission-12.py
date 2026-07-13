class DSU:
    def __init__(self, n):
        self.forests = n
        self.parent = list(range(n+1))
        self.rank = [1] * (n+1)
    
    def find(self, u):
        p = u

        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        
        return p
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)

        if pu == pv:
            return False
        
        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pv] < self.rank[pu]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
        
        self.forests -= 1
        return True
    
    def forestCount(self):
        return self.forests

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n-1:
            return False

        dsu = DSU(n)

        for u,v in edges:
            if not dsu.union(u,v):
                return False
        
        return dsu.forestCount() == 1