class Solution:
    def dfs(self, grid, row, col):
        if (
            row < 0 or col < 0 or
            row >= self.ROWS or col >= self.COLS or 
            (row,col) in self.visitedDFS or 
            grid[row][col] == 0
        ):
            return 0
        
        self.visitedDFS.add((row,col))
        
        area = 1
        for dr, dc in self.directions:
            nr, nc = row + dr , col + dc
            area += self.dfs(grid, nr, nc)
        
        return area
    
    def bfs(self, grid, row, col):
        q = deque()

        self.visitedBFS.add((row,col))
        q.append((row,col))
        currArea = 1

        while q:
            levelLen = len(q)
            for _ in range(levelLen):
                r, c = q.popleft()

                for dr,dc in self.directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < self.ROWS and
                        0 <= nc < self.COLS and
                        (nr,nc) not in self.visitedBFS and
                        grid[nr][nc] == 1
                    ):
                        self.visitedBFS.add((nr,nc))
                        q.append((nr,nc))
                        currArea += 1
        return currArea

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.ROWS, self.COLS = len(grid), len(grid[0])
        self.visitedDFS = set()
        self.visitedBFS = set()
        self.directions = [
            (0,1), (0,-1), (1,0), (-1,0)
        ]
        
        maxArea = 0
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if grid[r][c] == 1 and (r,c) not in self.visitedBFS:
                    currArea = self.bfs(grid,r,c)
                    maxArea = max(maxArea,currArea)
        
        return maxArea