class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] = min number of coins needed to make the amount i
        dp = [float('inf')] * (amount+1) # needs to be large for min to work
        
        dp[0] = 0 # to make a min amount of 0 you need no coins

        for currAmount in range(1,amount+1):
            for c in coins:
                if currAmount - c >= 0:
                    # Current min vs (1 new coin + coins needed for the remainder)
                    dp[currAmount] = min(dp[currAmount], 1 + dp[currAmount - c])
        
        return dp[amount] if dp[amount] != float('inf') else -1
