class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def isValid(r,c):
            return (
                0 <= r < R and
                0 <= c < C and 
                (r,c) not in visited and
                grid[r][c] == 2147483647
            )    
        
        visited =  set()
        q = deque()
        R, C = len(grid), len(grid[0])
        for r in range(R):
            for c in range(C):
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

                if isValid(nr,nc):
                    visited.add((nr,nc))
                    q.append((nr,nc,dist+1))           
        
        