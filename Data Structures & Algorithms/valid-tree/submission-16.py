class DSU:
    def __init__(self,n):
        self.forests = n
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, u):
        parentU = u

        while parentU != self.parent[parentU]:
            self.parent[parentU] = self.parent[self.parent[parentU]]
            parentU = self.parent[parentU]
        
        return parentU


    def union(self, u, v):
        parentU, parentV = self.find(u), self.find(v)

        if parentU == parentV:
            return False
        

        if self.rank[parentU] < self.rank[parentV]:
            self.parent[parentU] = parentV
        elif self.rank[parentV] < self.rank[parentU]:
            self.parent[parentV] = parentU
        else:
            self.parent[parentU] = parentV
            self.rank[parentV] += 1

        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        dsu = DSU(n)

        for u,v in edges:
            if not dsu.union(u,v):
                return False
        
        return True
