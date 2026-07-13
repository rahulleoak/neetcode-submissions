class Solution:
    def dfs(self, grid, row, col):
        if (
            row < 0 or col < 0 or
            row >= self.ROWS or col >= self.COLS or
            grid[row][col] == 1 or (row,col) in self.visited
        ):
            return 0
        
        if row == self.ROWS - 1 and col == self.COLS - 1:
            return 1
        
        self.visited.add((row,col))
        
        count = 0
        for dr, dc in self.directions:
            count += self.dfs(grid, row + dr, col + dc)
        
        self.visited.remove((row,col))
        return count


    def countPaths(self, grid: List[List[int]]) -> int:
        self.ROWS , self.COLS = len(grid), len(grid[0])
        self.visited = set()
        self.directions = [ [1,0], [-1,0], [0,1], [0,-1]]

        return self.dfs(grid,0,0)

