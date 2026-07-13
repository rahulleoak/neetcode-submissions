class Solution:
    def bfs(self, u, v):
        q = deque()
        visited = set()
    
        visited.add(u)
        q.append(u)

        while q:
            curr = q.popleft()
            
            if curr == v:
                return True

            for nei in self.adjList[curr]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
        
        return False
            
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.adjList = defaultdict(list)

        for u,v in edges:
            if u in self.adjList and v in self.adjList:
                if self.bfs(u,v):
                    return [u,v]
            
            self.adjList[u].append(v)
            self.adjList[v].append(u)
        
        return []