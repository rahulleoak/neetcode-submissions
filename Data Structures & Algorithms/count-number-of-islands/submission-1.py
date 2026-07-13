class Solution:
    def bfs(self, grid, row, col):
        q = collections.deque()
        self.visited.add((row,col))
        q.append((row,col))

        while q:
            levelLen = len(q)
            for _ in range(levelLen):
                r,c  = q.popleft()

                for dr, dc in self.directions:
                    nr, nc = r + dr, c + dc

                    if (
                        nr >= 0 and nc >= 0 and
                        self.ROWS > nr and self.COLS > nc and
                        (nr,nc) not in self.visited and 
                        grid[nr][nc] == '1'
                    ):
                        self.visited.add((nr,nc))
                        q.append((nr,nc))


    def numIslands(self, grid: List[List[str]]) -> int:
        self.ROWS, self.COLS = len(grid) , len(grid[0])
        self.directions = [
            (0,1), (0,-1), (1,0), (-1,0)
        ]       
        self.visited = set()

        numOfIslands = 0
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if grid[r][c] == '1' and (r,c) not in self.visited:
                    self.bfs(grid, r, c)
                    numOfIslands += 1

        return numOfIslands