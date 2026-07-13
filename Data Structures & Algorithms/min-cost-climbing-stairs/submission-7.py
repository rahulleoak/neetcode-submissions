'''
S: let dp[i] be the min cost to reach the i-th step

R: 
To reach the i-th step, we must have come from i-1 or i-2
At the i-th step, we want to know the MIN cost it takes to reach here.
So dp[i] = cost[i] + min(dp[i-1], dp[i-2])

T: Problems should be solved in increasing order

B: dp[0] = cost[0], dp[1] = cost[1]

O: dp[n]

T: O(n)

'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n)
        dp[0], dp[1] = cost[0], cost[1]

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-2], dp[i-1])
        
        return min(dp[-1], dp[-2])

        '''
        # Memoization
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
        '''