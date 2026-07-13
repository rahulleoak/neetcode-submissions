class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n, res = len(grid), len(grid[0]), 0 
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    res += (r + 1 >= m or grid[r+1][c] == 0) 
                    res += (c + 1 >= n or grid[r][c+1] == 0)  
                    res += (r - 1 < 0 or grid[r-1][c] == 0) 
                    res += (c - 1 < 0 or grid[r][c-1] == 0)
        
        return res
                