class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp = [0] * (capacity + 1)

        for i in range(len(weight)):
            for w in range(capacity, weight[i] - 1, -1):
                dp[w] = max(dp[w], profit[i] + dp[w - weight[i]])
        
        return dp[capacity]