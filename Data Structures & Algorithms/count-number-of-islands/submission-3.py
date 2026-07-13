class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.R = len(grid)
        self.C = len(grid[0])

        visited = set()

        def inBounds(r,c):
            return 0 <= r < self.R and 0 <= c < self.C
        def validCell(r,c):
            return grid[r][c] == "1" and (r,c) not in visited
        

        DIR = [(0,1),(1,0),(0,-1),(-1,0)]

        def dfs(r,c):
            
            
            visited.add((r,c))

            for dr, dc in DIR:
                nr, nc = dr + r, dc + c
                if inBounds(nr,nc) and validCell(nr,nc):
                    dfs(nr,nc)
                    
        islandCount = 0
        for r in range(self.R):
            for c in range(self.C):
                if validCell(r,c):
                    dfs(r,c)
                    islandCount += 1

        return islandCount