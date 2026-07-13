class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Let dp[i] = The total number of combinations that make the amount 'i'
        dp = [0] * (amount+1)
        # BASE CASE: Initialize to 0. There is exactly 1 way to make amount 0 (use nothing).
        dp[0] = 1
        
        # TOPOLOGICAL ORDER: Unbounded template (Forwards
        for c in coins:
            for amt in range(c, amount+1):
                # RELATION: Accumulate the ways to make the current amount
                dp[amt] = dp[amt - c] + dp[amt]
        
        return dp[amount]
