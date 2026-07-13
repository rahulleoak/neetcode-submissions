class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        totalSum = sum(stones)
        target = totalSum // 2

        # Let dp[i] be the max sum of stones that does not exceed capacity i.
        dp = [0] * (target + 1)

        for stone in stones:
            for subsetSum in range(target, stone-1, -1):
                skip = dp[subsetSum]
                take = dp[subsetSum - stone] + stone
                dp[subsetSum] = max(dp[subsetSum], dp[subsetSum - stone] + stone)
        
        return abs((dp[target] * 2) - totalSum)