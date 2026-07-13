class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        S: dp[i] = # of ways to achieve step 'i'
        
        R: 
        To reach dp[i] we must have either come from one step down (i-1) or two steps down (i-2)
        So to find the total number of ways to reach step 'i', we add the solutions of the subproblem
            => dp[i] = dp[i-2] + dp[i-1]
        
        T: Need to go in increasing step order
        
        B: dp[0] = 0, dp[1] = 1, dp[2] = 2
        
        O: dp[n]
        
        T: O(n)
        '''
        
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