class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def isValid(r, c, visited):
            return (
                0 <= r < R and
                0 <= c < C and
                (r,c) not in visited 
            )
        
        def bfs(q, visited):
            while q:
                r, c = q.popleft()

                for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                    nr, nc = dr + r, dc + c

                    if isValid(nr,nc, visited) and heights[nr][nc] >= heights[r][c]:
                        visited.add((nr,nc))
                        q.append((nr,nc))
        
        R, C = len(heights), len(heights[0])
        visitedP, visitedA = set(), set()
        qP, qA = deque(), deque()

        for r in range(R):
            visitedP.add((r,0))
            qP.append((r,0))

            visitedA.add((r, C-1))
            qA.append((r, C-1))
        
        for c in range(C):
            visitedP.add((0,c))
            qP.append((0,c))

            visitedA.add((R-1,c))
            qA.append((R-1,c))
        
        bfs(qP, visitedP)
        bfs(qA, visitedA)

        return [[r,c] for r, c in visitedP if (r,c) in visitedA]
        
