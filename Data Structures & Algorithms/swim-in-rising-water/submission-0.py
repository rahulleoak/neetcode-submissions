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
        pq = [(grid[0][0], 0, 0)] # [val@cell, r, c]
        directions = [
            (0,1), (0,-1), (1,0), (-1,0) 
        ]
        visited = set()

        while pq:
            currVal, r, c = hq.heappop(pq)

            visited.add((r,c))

            if r == n-1 == c:
                return currVal

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if self.isValid(n, nr, nc, visited):
                    newRainCandidate = max(currVal, grid[nr][nc])
                    hq.heappush(pq, (newRainCandidate , nr, nc))