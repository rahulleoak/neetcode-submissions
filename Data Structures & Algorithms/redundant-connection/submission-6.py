class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adjList = {i : [] for i in range(n+1)}
        for src, dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)
        
        
        visited = set()
        cycleNode = -1
        cycleEdge = set()

        def dfs(node, par):
            nonlocal cycleNode

            if node in visited:
                cycleNode = node
                return True
            
            visited.add(node)

            for nei in adjList[node]:
                if nei == par:
                    continue
                
                if dfs(nei, node):
                    if cycleNode != -1:
                        cycleEdge.add(node)
                    if cycleNode == node:
                        cycleNode = -1
                
                    return True
            return False
        
        edge = dfs(1,-1)
        if not edge:
            return []
        

        for u,v in reversed(edges):
            if u in cycleEdge and v in cycleEdge:
                return [u,v]
        
            