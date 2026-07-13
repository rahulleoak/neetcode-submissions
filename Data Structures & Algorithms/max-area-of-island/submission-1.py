class Solution:
    def dfs(self, grid, row, col):
        if (
            0 > row or 0 > col or
            row >= self.ROWS or col >= self.COLS or
            grid[row][col] == 0 
        ):
            return 0
        
        grid[row][col] = 0

        area = 1

        for dr, dc in self.directions:
            area += self.dfs(grid, row + dr, col + dc)
        
        return area


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.ROWS = len(grid)
        self.COLS = len(grid[0])
        self.directions = [ [1,0], [-1,0], [0,1], [0,-1]]

        maxArea = 0
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if grid[r][c] == 1:
                    currArea = self.dfs(grid,r,c)
                    maxArea = max(maxArea , currArea)
        
        return maxArea