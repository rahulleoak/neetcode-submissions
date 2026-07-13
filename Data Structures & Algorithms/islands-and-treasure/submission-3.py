class Solution:
    def isValid (self, r, c, rRange, cRange, visited, grid):
        return (
            0 <= r < rRange and
            0 <= c < cRange and
            (r,c) not in visited and
            grid[r][c] == 2147483647
        )

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return grid
        
        q = deque()        
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visited.add((r,c))
                    q.append((r,c,0))
        
        if not q:
            return grid
        
        directions = [
            (0,1), (1,0), (0,-1), (-1,0)
        ]

        while q:
            r, c, dist = q.popleft()

            grid[r][c] = dist

            for dr, dc in directions:
                nr, nc = dr + r, dc + c

                if self.isValid(nr, nc, ROWS, COLS, visited, grid):
                    visited.add((nr,nc))
                    q.append((nr,nc, dist + 1))
        

