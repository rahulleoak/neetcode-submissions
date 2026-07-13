class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [
            (0,1), (1,0), (-1,0), (0,-1)
        ]

        def isValid(r, c):
            return (
                0 <= r < ROWS and
                0 <= c < COLS and
                grid[r][c] == 1
            )
        
        def dfs(r, c):
            if not isValid(r, c):
                return 0
            
            grid[r][c] = 0 
            
            area = 1
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                area += dfs(nr,nc)
            
            return area
        
        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    currArea = dfs(r,c)
                    if currArea > maxArea:
                        maxArea = currArea
        
        return maxArea
