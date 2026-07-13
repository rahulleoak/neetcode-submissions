from functools import lru_cache

class Solution:
    @lru_cache(maxsize = 10000)
    def memoization(self, r, c):
        if r >= self.ROWS or c >= self.COLS:
            return 0 
        
        if r == self.ROWS - 1 and c == self.COLS - 1:
            return 1
        
        return self.memoization(r+1,c) + self.memoization(r,c+1)


    def uniquePaths(self, m: int, n: int) -> int:
        self.ROWS, self.COLS = m , n

        return self.memoization(0,0)