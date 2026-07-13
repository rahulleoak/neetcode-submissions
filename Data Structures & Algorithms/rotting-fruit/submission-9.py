class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def isValid(r,c):
            return (
                0 <= r < R and
                0 <= c < C and
                (r,c) not in visited and
                grid[r][c] == 1
            )
        
        R, C = len(grid), len(grid[0])
        fresh = 0
        visited = set()
        q = deque()
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    visited.add((r,c))
                    q.append((r,c))

        if not fresh:
            return 0
        if not len(q):
            return -1


        time = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                    nr, nc = dr + r, dc + c

                    if isValid(nr,nc):
                        visited.add((nr,nc))
                        q.append((nr,nc))
                        fresh -= 1
            time += 1

        
        return time if fresh == 0 else -1
