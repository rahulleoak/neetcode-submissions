from functools import lru_cache
class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        def dfs(i):
            if i > n:
                return 0

            if i == n:
                return 1
            
            return dfs(1 + i) + dfs(2 + i)
        
        return dfs(0)
            