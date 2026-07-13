class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False
        target = totalSum // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for n in nums:
            for currTarget in range(target, n-1, -1):
                dp[currTarget] = dp[currTarget] or dp[currTarget - n]
        
        return dp[target]