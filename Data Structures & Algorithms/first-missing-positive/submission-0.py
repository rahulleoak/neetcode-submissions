class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for idx in range(n):
            if nums[idx] <= 0:
                nums[idx] = n + 1
        
        for idx, val in enumerate(nums):
            targetVal = abs(val)

            if 0 < targetVal <= n:          
                targetIdx = targetVal - 1
                if nums[targetIdx] > 0:
                    nums[targetIdx] *= -1


        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        return n+1