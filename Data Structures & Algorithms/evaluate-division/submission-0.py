class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = defaultdict(list)

        for i, variables in enumerate(equations):
            a, b = variables
            adjList[a].append((b, values[i]))
            adjList[b].append((a, 1 / values[i]))

        def bfs(src, target):
            if src not in adjList or target not in adjList:
                return -1
                        
            q = deque()
            q.append((src, 1))
            
            visited = set()
            visited.add(src)

            while q:
                node, value = q.popleft()

                if node == target:
                    return value

                for nei, weight in adjList[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, value * weight))
                
            return -1
                

        res = []
        for u, v in queries:
            res.append(bfs(u,v))
        
        return res