class Solution:
    def isValid(self, r, c):
        return (
            0 <= r < self.R and
            0 <= c < self.C and
            self.grid[r][c] == 1
        )
    
    def dfs(self, r, c):
        if not self.isValid(r,c):
            return 0
        
        self.grid[r][c] = 0

        area = 1
        for dr, dc in self.directions:
            nr, nc = dr + r, dc + c
            area += self.dfs(nr,nc)
        
        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.R, self.C = len(grid), len(grid[0]) 
        self.grid = grid
        self.directions = [
            (0,1), (1,0), (0,-1), (-1,0)
        ]
        
        maxArea = 0
        for r in range(self.R):
            for c in range(self.C):
                if grid[r][c] == 1:
                    area = self.dfs(r,c)
                    if area > maxArea:
                        maxArea = area
        
        return maxArea


