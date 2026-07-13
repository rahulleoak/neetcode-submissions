class Solution:
    def bfs(self, grid, queue, visited):
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                visited.add((row,col))

            
                for dr,dc in self.directions:
                    nr, nc = row + dr, col + dc
                    if (
                        0 <= nr < self.ROWS and
                        0 <= nc < self.COLS and
                        (nr,nc) not in visited and
                        grid[nr][nc] >= grid[row][col]
                    ):
                        visited.add((nr,nc))
                        queue.append((nr,nc))
                 

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.ROWS, self.COLS = len(heights), len(heights[0])
        self.directions = [
            (0,1), (0,-1), (1,0), (-1,0)
        ]
        self.pacificSet, self.atlanticSet = set(), set()

        pacificQ, atlanticQ = deque(), deque()


        for c in range(self.COLS):
            pacificQ.append((0, c))
            atlanticQ.append((self.ROWS - 1, c))
        for r in range(self.ROWS):
            pacificQ.append((r, 0))
            atlanticQ.append((r, self.COLS - 1))

        self.bfs(heights, pacificQ, self.pacificSet)
        self.bfs(heights, atlanticQ, self.atlanticSet)

        res = []
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if (r,c) in self.pacificSet and (r,c) in self.atlanticSet:
                    res.append([r,c])
        
        return res