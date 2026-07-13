class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def isValid(r,c):
            return 0 <= r < R and 0 <= c < C and (r,c) not in visited and grid[r][c] == 2147483647
        
        
        directions = [
            (0,1), (1,0), (0,-1), (-1,0)
        ]

        R, C = len(grid), len(grid[0])
        visited = set()

        q = deque()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    visited.add((r,c))
                    q.append((r,c))

        

        distance = 1
        while q:
            for _ in range(len(q)):
                room = q.popleft()
                r,c = room

                for dr,dc in directions:
                    nr, nc = dr + r, dc + c
                    if isValid(nr,nc):
                        visited.add((nr,nc))
                        q.append((nr,nc))
                        grid[nr][nc] = distance
            
            distance += 1


        
