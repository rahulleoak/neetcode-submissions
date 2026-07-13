class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        totalSum = sum(stones)
        target =  totalSum // 2 # capacity

        dp = [0] * (target + 1) # 1-idx

        for stone in stones:
            for currTarget in range(target, stone-1, -1):
                if currTarget - stone >= 0:
                    take = dp[currTarget - stone] + stone
                    skip = dp[currTarget]
                    dp[currTarget] = max(take, skip)
        
        return totalSum - (dp[target] * 2) 