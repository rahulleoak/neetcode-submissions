class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(idx):
            if idx >= n:
                return idx == n
            
            if idx in memo:
                return memo[idx]          

            memo[idx] = dfs(idx+1) + dfs(idx+2)
            
            return memo[idx]
        
        return dfs(0)