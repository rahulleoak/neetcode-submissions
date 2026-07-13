class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def isValid(r,c,R,C):
            return (
                0 <= r < R and
                0 <= c < C and
                grid[r][c] == "1"
            )
        
        def dfs(r,c):
            if not isValid(r,c,R,C):
                return
            
            grid[r][c] = "0"

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                dfs(nr,nc)
                
        R, C = len(grid), len(grid[0])
        directions = [
            (0,1), (1,0), (-1,0), (0,-1)
        ]

        islandCount = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islandCount += 1
        
        return islandCount
         