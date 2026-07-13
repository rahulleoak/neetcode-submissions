import heapq as hq

class Solution:
    def isValid(self, n, r, c, visited):
	    return (
            0 <= r < n and
            0 <= c < n and
            (r,c) not in visited
        )
    
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [
            (0,1), (0,-1), (1,0), (-1,0) 
        ]

        pq = [(grid[0][0], 0, 0)] # [time/max height so far, r, c]
        visited = set()
        # visited.add((0,0))

        while pq:
            maxHeight, r, c = hq.heappop(pq)

            visited.add((r,c))

            if r == n-1 == c:
                return maxHeight

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if self.isValid(n, nr, nc, visited):
                    newRainCandidate = max(maxHeight, grid[nr][nc])
                    # visited.add((nr,nc))
                    hq.heappush(pq, (newRainCandidate , nr, nc))