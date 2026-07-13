class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * (n)
        
        for nxt in range(n):
            for idx in range(nxt):
                if nums[nxt] > nums[idx]:
                    # dp[nxt] = max of either itself or the max at 'idx' plus 1 (to include "nxt")
                    dp[nxt] = max(dp[idx] + 1, dp[nxt])
        
        return max(dp)
