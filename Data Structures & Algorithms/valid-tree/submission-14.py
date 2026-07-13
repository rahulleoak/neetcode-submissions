class DSU:
    def __init__(self, n):
        self.forests = n
        self.rank = [1] * n
        self.parent = list(range(n))

    def find(self, u):
        p = u 
        while self.parent[p] != p:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        
        return p
    
    def union(self, u, v):
        pU, pV = self.find(u), self.find(v)

        if pU == pV:
            return False
        
        if self.rank[pU] < self.rank[pV]:
            self.parent[pU] = pV
        elif self.rank[pV] < self.rank[pU]:
            self.parent[pV] = pU
        else:
            self.parent[pV] = pU
            self.rank[pU] += 1
        
        self.forests -= 1
        return True
    
    def forestCount(self):
        return self.forests

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        
        dsu = DSU(n)

        for u,v in edges:
            if not dsu.union(u,v):
                return False
        
        return dsu.forestCount() == 1