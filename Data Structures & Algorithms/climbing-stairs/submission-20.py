class Solution:
    def climbStairs(self, n: int) -> int:
        memo = defaultdict(int)

        def dfs(step):
            if step == n:
                return 1
            if step > n:
                return 0
            if step in memo:
                return memo[step]
            
            memo[step] += dfs(step + 1)
            memo[step] += dfs(step + 2)
            
            return memo[step]

        return dfs(0)