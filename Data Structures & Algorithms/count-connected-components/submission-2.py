class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {x : [] for x in range(n)}
        for src, dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for nei in adjList[node]:
                dfs(nei)
        
        visited = set()
        count = 0 
        for x in range(n):
            if x not in visited:
                dfs(x)
                count += 1
        
        return count