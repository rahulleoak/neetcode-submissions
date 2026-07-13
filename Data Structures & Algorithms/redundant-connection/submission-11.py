class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        parentMap = {i: None for i in range(1, n + 1)}  # None => undiscovered
        cycle_edges = set()

        def dfs(node, parent):
            """
            Returns:
              - None if no cycle found in this subtree
              - anchor node id of the cycle if a back-edge was found
            While unwinding, add edges to cycle_edges until we reach the anchor.
            """
            if parentMap[node] is not None:
                return node

            # discover node
            parentMap[node] = parent

            for nei in adjList[node]:
                if nei == parent:
                    continue  # skip the edge back to parent

                anchor = dfs(nei, node)
                if anchor is None:
                    continue  # no cycle in that branch

                # We are on the cycle path; record this edge (node, nei)
                cycle_edges.add((node, nei))
                # If u is the anchor, we've completed the cycle marking; stop bubbling it up
                if anchor == node:
                    return None  # signal: done marking cycle
                else:
                    return anchor  # keep propagating the anchor upward

            return None  # no cycle from u
        
        start = edges[0][0]
        dfs(start,-1)

        for u,v in reversed(edges):
            if (u,v) in cycle_edges or (v,u) in cycle_edges:
                return [u,v]
        return []