class Graph:
    
    def __init__(self):
        self.adjList = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adjList:
            self.adjList[src] = set()
        if dst not in self.adjList:
            self.adjList[dst] = set()
        
        self.adjList[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adjList or dst not in self.adjList:
            return False
        
        self.adjList[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        if src not in self.adjList or dst not in self.adjList:
            return False
        
        return self.bfs(src, dst)
    
    def bfs(self, src, dst):
        visited = set([src])
        q = deque([src])

        while q:
            node = q.popleft()

            if node == dst:
                return True
            
            for nei in self.adjList[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
        
        return False


