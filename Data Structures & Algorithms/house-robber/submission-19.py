'''
S: Let dp[i] represent the max profit from robbing upto "i" houses

R:
dp[i] is dependent on the max profit of dp[i-1] (adj) and dp[i-2] (far) houses.
if adj -> we would NOT include the cost[i]
if far -> we would include the cost[i]
Hence => dp[i] = max(dp[i-1], dp[i-2] + cost[i]) 

T: Solve in increasing 

B: dp[0] = cost[0], dp[1] = max(cost[0], cost[1])

O: dp[n]

T: O(n)
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        far, adj = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            maxProfit = max(far + nums[i], adj)

            far = adj
            adj = maxProfit
        
        return adj
        
        
        ''' 
        # Tabulation

        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            far = dp[i-2] + nums[i]
            adj = dp[i-1]

            dp[i] = max(far,adj)
        
        return dp[-1]
        '''
        
        '''
        Memoization

        memo = {}
        def dfs(idx):
            if idx >= len(nums):
                return 0
            if idx in memo:
                return memo[idx]         
            
            skip = dfs(idx + 1)
            take = nums[idx] + dfs(idx + 2)

            memo[idx] =  max(skip, take)

            return memo[idx]
        
        return max(dfs(0), dfs(1))
        '''