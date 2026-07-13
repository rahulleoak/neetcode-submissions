class Solution:
    def isValid(self, row, col, m, n, grid):
        return (
            0 <= row < m and
            0 <= col < n and
            grid[row][col] == 1
        )


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        directions = [
            (0,1), (1,0), (-1,0), (0,-1)
        ]

        def dfs(r,c):
            if not self.isValid(r,c,m,n,grid):
                return 0
            
            grid[r][c] = 0
            area = 1
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                area += dfs(nr,nc)
            
            return area

        maxArea = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    currArea = dfs(r,c)
                    if currArea > maxArea:
                        maxArea = currArea

        return maxArea