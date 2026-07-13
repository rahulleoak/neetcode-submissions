class Solution:
    def isValid(self, row, col, m, n, visited):
        return (
            0 <= row < m and
            0 <= col < n and
            (row,col) not in visited
        )

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        
        q = deque()
        visited = set()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    visited.add((r,c))
                    q.append((r,c,0))
                    
        if len(q) == 0:
            return grid
        
        directions = [
            (0,1), (1,0), (-1,0), (0,-1)
        ]

        while q:
            r, c, dist = q.popleft()

            grid[r][c] = dist
            
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if self.isValid(nr,nc,m,n,visited) and grid[nr][nc] == 2147483647:
                    visited.add((nr,nc))
                    q.append((nr,nc,dist+1))
        

