class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dfs(idx):
            if idx >= len(cost):
                return 0
            if idx in memo:
                return memo[idx]

            oneJump = cost[idx] + dfs(idx + 1)
            twoJump = cost[idx] + dfs(idx + 2)

            memo[idx] = min(oneJump, twoJump)
            
            return memo[idx]

        return min(dfs(0), dfs(1))