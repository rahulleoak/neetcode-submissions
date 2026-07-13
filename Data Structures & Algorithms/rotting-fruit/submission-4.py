class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        
        ROWS, COLS = len(grid), len(grid[0])
        DIR4 = [(0,1),(1,0),(0,-1),(-1,0)]
        def isValid(r,c):
            return 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 1
        
        freshFruit = 0
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    freshFruit += 1
        
        if freshFruit == 0:
            return 0
        if not len(q):
            return -1
        
        
        time = -1
        while q:
            levelLen = len(q)
            for _ in range(levelLen):
                r, c = q.popleft()

                for dr, dc in DIR4:
                    nr, nc = dr + r, dc + c
                    if isValid(nr,nc):
                        grid[nr][nc] = 2
                        freshFruit -= 1
                        q.append((nr,nc))
            time += 1
        
        return time if freshFruit == 0 else -1


                
