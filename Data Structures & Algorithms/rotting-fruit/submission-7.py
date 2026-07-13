class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [
            (0,1), (1,0), (0,-1), (-1,0)
        ]

        def isValid(r,c):
            return (
                0 <= r < ROWS and 
                0 <= c < COLS and
                grid[r][c] == 1
            )

        q = deque()
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
        if fresh == 0:
            return 0
        if not len(q):
            return -1
        
        time = 0
        while q and fresh > 0:
            levelLen = len(q)
            for _ in range(levelLen):
                r, c = q.popleft()
            
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if isValid(nr,nc):
                        fresh -= 1
                        grid[nr][nc] = 2
                        q.append((nr,nc))
            time += 1

        return time if fresh == 0 else -1
        
