class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [
            (0,1), (0,-1), (1,0), (-1,0)
        ]
        visited = set()
        
        q = deque()
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    visited.add((r,c))
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1

        time =  0
        while q and fresh > 0:
            levelLen = len(q)
            for _ in range(levelLen):
                row, col = q.popleft()
            
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if (
                        0 <= nr < ROWS and
                        0 <= nc < COLS and
                        (nr,nc) not in visited and
                        grid[nr][nc] == 1
                    ):
                        visited.add((nr,nc))
                        q.append((nr,nc))
                        fresh -= 1      
            
            time += 1
        

        return time if fresh == 0 else -1
                    