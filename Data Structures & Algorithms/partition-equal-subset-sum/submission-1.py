class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 == 1:
            return False
        
        target = totalSum // 2
        n = len(nums)
        prevDP = [False] * (target+1)
        prevDP[0] = True

        for numIdx in range(1, n+1):
            dp = [False] * (target+1)
            
            for currSum in range(1, target+1):
                if nums[numIdx-1] <= currSum:
                    remaining = currSum - nums[numIdx-1]
                    dp[currSum] = prevDP[currSum] or prevDP[remaining]
                else:
                    dp[currSum] = prevDP[currSum]

            prevDP = dp
        
        return prevDP[target]