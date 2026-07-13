class Solution:            
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        self.adjList = {i:[] for i in range(n)}
        self.visited = set()

        for src, dst in edges:
            self.adjList[src].append(dst)
            self.adjList[dst].append(src)

        q = deque()
        self.visited.add(0)
        q.append(0)

        while q:
            curr = q.popleft()
             
            for v in self.adjList[curr]:
                if v not in self.visited:
                    self.visited.add(v)
                    q.append(v)
        
        return True if len(self.visited) == n else False