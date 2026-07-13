class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = float('inf')
        maxProfit = 0

        for sell in prices:
            minBuy = min(sell, minBuy)
            maxProfit = max(maxProfit, sell - minBuy)

        return maxProfit