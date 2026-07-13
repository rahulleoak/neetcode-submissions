class Solution:
    def isValid(self, r, c, m, n, visited):
        return (
            0 <= r < m and 
            0 <= c < n and
            (r,c) not in visited
        )

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(source, visited):
            q = deque(source)

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    if self.isValid(nr,nc, m, n, visited) and heights[nr][nc] >= heights[r][c]:
                        visited.add((nr,nc))
                        q.append((nr,nc))
        
        m, n = len(heights), len(heights[0])
        directions = [
            (0,1), (1,0), (-1,0), (0,-1)
        ]
        visitedP, visitedA = set(), set()
        pacificStart, atlanticStart = [], []

        for r in range(m):
            pacificStart.append((r,0))
            visitedP.add((r,0))

            atlanticStart.append((r, n-1))
            visitedA.add((r, n-1))
        
        for c in range(n):
            pacificStart.append((0,c))
            visitedP.add((0,c))

            atlanticStart.append((m-1, c))
            visitedA.add((m-1, c))

        bfs(pacificStart, visitedP)
        bfs(atlanticStart, visitedA)


        return [[r,c] for r in range(m) for c in range(n) if (r,c) in visitedP and (r,c) in visitedA]

