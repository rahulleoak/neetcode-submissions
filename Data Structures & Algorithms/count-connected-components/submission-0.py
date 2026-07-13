class Solution:
    def bfs(self, node):
        q = deque()
        self.visited.add(node)
        q.append(node)
        
        while q:
            levelLen = len(q)
            for _ in range(levelLen):
                curr = q.popleft()
                for nei in self.adjList[curr]:
                    if nei not in self.visited:
                        self.visited.add(nei)
                        q.append(nei)
        

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.adjList = {i : [] for i in range(n)}
        for u, v in edges:
            self.adjList[u].append(v)
            self.adjList[v].append(u)
        
        self.visited = set()

        componentCount = 0
        for node in range(n):
            if node not in self.visited:
                self.bfs(node)
                componentCount += 1
        
        return componentCount


