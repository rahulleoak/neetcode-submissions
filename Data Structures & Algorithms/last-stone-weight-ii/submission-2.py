class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        totalSum = sum(stones)
        target = totalSum // 2

        dp = [0] * (target + 1)

        for stone in stones:
            for subsetSum in range(target, stone-1, -1):
                dp[subsetSum] = max(dp[subsetSum], dp[subsetSum - stone] + stone)
        
        return totalSum - (dp[target] * 2)