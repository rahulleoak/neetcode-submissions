class Solution:
    def dfs(self, node, parent):
        if node in self.visited:
            return False 
        
        self.visited.add(node)
        
        for v in self.adjList[node]:
            if v not in self.visited:
                if not self.dfs(v,node):
                    return False
            elif v != parent:
                return False
        
        return True
    
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.visited = set()
        self.adjList = {i: [] for i in range(n)}
        for u,v in edges:
            self.adjList[u].append(v)
            self.adjList[v].append(u)
        
        

        return self.dfs(0,-1) and len(self.visited) == n

