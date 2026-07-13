class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)

        if totalSum % 2 != 0:
            return False
        
        target = totalSum // 2

        dp = [[False] * (target+1) for _ in range(len(nums)+ 1)]
        for r in range(len(nums)+1):
            dp[r][0] = True
        
        for numIdx in range(1, len(nums)+1):
            for currSum in range(1, target+1):
                if nums[numIdx-1] <= currSum:
                    remaining = currSum - nums[numIdx-1]
                    dp[numIdx][currSum] = dp[numIdx-1][currSum] or dp[numIdx-1][remaining]
                else:
                    dp[numIdx][currSum] = dp[numIdx-1][currSum]
        
        return dp[len(nums)][target]