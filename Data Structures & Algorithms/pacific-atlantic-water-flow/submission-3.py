class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        visitedP, visitedA = set(), set()
        qP, qA = deque(), deque()
        ROWS, COLS = len(heights), len(heights[0])
        DIR4 = [
            (0,1), (1,0), (-1,0), (0,-1)
        ]

        def isValid(r, c, visited):
            return (
                0 <= r < ROWS and
                0 <= c < COLS and
                (r,c) not in visited
            )
        
        def BFS(q, visited):
            while q:
                r, c = q.popleft()

                for dr, dc in DIR4:
                    nr, nc = dr + r, dc + c

                    if (
                        isValid (nr, nc, visited) and
                        heights[nr][nc] >= heights[r][c]
                    ):
                        visited.add((nr,nc))
                        q.append((nr,nc))
            
            return visited

        for r in range(ROWS):
               visitedP.add((r,0))
               qP.append((r,0))

               visitedA.add((r, COLS-1))
               qA.append((r, COLS-1))
        
        for c in range(COLS):
            visitedP.add((0, c))
            qP.append((0, c))

            visitedA.add((ROWS-1, c))
            qA.append((ROWS-1, c))

        visitedP, visitedA = BFS(qP, visitedP), BFS(qA, visitedA)

        return [[r,c] for r, c in visitedP if (r,c) in visitedA]
