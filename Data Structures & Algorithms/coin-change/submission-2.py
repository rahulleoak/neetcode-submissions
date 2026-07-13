class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0


        for idx in range(1, len(dp)):
            for c in coins:
                if idx - c >= 0:
                    dp[idx] = min(dp[idx], 1 + dp[idx - c])

        
        return dp[amount] if dp[amount] != amount+1 else -1
        