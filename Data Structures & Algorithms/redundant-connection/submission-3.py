class DSU:
    def __init__(self,N):
        self.N = N
        self.parent = {}
        self.rank = defaultdict(int)
        for i in range(N+1):
            self.rank[i] = 1
            self.parent[i] = i
    
    def find(self, vertex):
        p = self.parent[vertex]

        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        
        return p
    
    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)

        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        dsu = DSU(N)

        for n1, n2 in edges:
            if not dsu.union(n1,n2):
                return [n1,n2]