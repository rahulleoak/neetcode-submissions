class Solution:
    def isValid(self, row, col, m, n, grid):
        return (
            0 <= row < m and 
            0 <= col < n and 
            grid[row][col] == "1"
        )

    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [
            (0,1), (1,0), (0,-1), (-1,0)
        ]

        def dfs(r, c):
            if not self.isValid(r, c, rows, cols, grid):
                return 
            
            grid[r][c] = "0"

            for dr, dc in directions:
                nr , nc = dr + r, dc + c
                dfs(nr, nc)
        
        islandCount = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islandCount += 1
            

        return islandCount


        
        