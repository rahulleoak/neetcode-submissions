class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        visited = set()
        cycleSet = set()

        def dfs(node, parent):
            """
            Returns:
              - None if no cycle found in this subtree
              - anchor node id of the cycle if a back-edge was found
            While unwinding, add nodes to cycleSet until we reach the anchor.
            """
            if node in visited:
                return node

            # discover node
            visited.add(node)

            for nei in adjList[node]:
                if nei == parent:
                    continue  # skip the edge back to parent

                anchor = dfs(nei, node)
                if anchor is None:
                    continue  # no cycle in that branch

                # We are on the cycle path; record this node
                cycleSet.add(node)
                # If node is the anchor, we've completed the cycle marking; stop bubbling it up
                if anchor == node:
                    return None  
                return anchor

            return None  # no cycle formed
        
        start = edges[0][0]
        dfs(start,-1)

        for u,v in reversed(edges):
            if u in cycleSet and v in cycleSet:
                return [u,v]