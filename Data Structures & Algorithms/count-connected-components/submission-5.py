class DSU:
    def __init__(self, n):
        self.forests = n
        self.parents = {}
        self.rank = {}

        for i in range(n):
            self.parents[i] = i
            self.rank[i] = 1
    
    def find(self, u):
        parent = u

        while self.parents[parent] != parent:
            self.parents[parent] = self.parents[self.parents[parent]]
            parent = self.parents[parent]
    
        return parent
    

    def union(self, u, v):
        pU, pV = self.find(u), self.find(v)

        if pU == pV:
            return
        
        if self.rank[pU] < self.rank[pV]:
            self.parents[pU] = pV
        elif self.rank[pV] < self.rank[pU]:
            self.parents[pV] = pU
        else:
            self.parents[pU] = pV
            self.rank[pV] += 1
        
        self.forests -= 1

        return
    
    def forestCount(self):
        return self.forests

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)

        for u, v in edges:
            dsu.union(u,v)
        
        return dsu.forestCount()