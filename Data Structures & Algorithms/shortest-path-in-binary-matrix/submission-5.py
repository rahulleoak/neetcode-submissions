class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[ROWS -1][COLS -1] == 1:
            return -1

        visited = set()
        q = deque()
        
        #Append r,c,startingPathLen
        q.append((0,0,1))
        visited.add((0,0))

        directions = [
            (0,1), (0,-1), (1,0), (-1,0), (1,1),(-1,-1), (1,-1), (-1,1)
        ]

        while q:
            levelLen = len(q)
            for _ in range(levelLen):
                r, c, pathLen = q.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return pathLen

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    if (
                        0 <= nr < ROWS and
                        0 <= nc < COLS and
                        grid[nr][nc] == 0 and
                        (nr,nc) not in visited
                    ):
                        q.append((nr,nc,pathLen + 1))
                        visited.add((nr,nc))
        
        return -1