class Solution:
    def dfs(self, grid, row, col):
        if (
            row < 0 or row >= self.ROWS or
            col < 0 or col >= self.COLS or
            grid[row][col] == '0'
        ):
            return 0

        grid[row][col] = '0'
        
        for dr,dc in self.directions:
            self.dfs(grid, row + dr, col + dc)

    def numIslands(self, grid: List[List[str]]) -> int:
        self.ROWS, self.COLS = len(grid), len(grid[0])
        self.directions = [
            (0,1), (0,-1), (1,0), (-1,0)
        ]
        
        if not grid:
            return 0

        numberOfIsland = 0
        for r in range(self.ROWS):
            for c in range (self.COLS):
                if grid[r][c] == '1':
                    self.dfs(grid,r,c)
                    numberOfIsland += 1
        
        return numberOfIsland
