class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        visited = set()
        parent = {}
        cycle_edges = set()
        found = False

        def mark_cycle(u, v):
            """record all undirected edges along path u -> ... -> v (inclusive)"""
            cycle_edges.add(tuple(sorted((u, v))))  # the back edge
            cur = u
            while cur != v:
                p = parent[cur]
                cycle_edges.add(tuple(sorted((cur, p))))
                cur = p

        def dfs(u, p):
            nonlocal found
            visited.add(u)
            for v in g[u]:
                if v == p:
                    continue
                if v in visited:
                    # found cycle
                    mark_cycle(u, v)
                    found = True
                    return
                parent[v] = u
                dfs(v, u)
                if found:
                    return

        # graph may be 1..n; start from any present node
        for node in g.keys():
            if node not in visited:
                parent[node] = 0
                dfs(node, 0)
                if found:
                    break

        # pick the last input edge that lies on the cycle
        ans = []
        for u, v in edges:
            if tuple(sorted((u, v))) in cycle_edges:
                ans = [u, v]
        return ans