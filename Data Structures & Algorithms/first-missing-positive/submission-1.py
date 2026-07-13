class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        i = 0        
        while i < n:
            val = nums[i]

            if 0 < val <= n and nums[val - 1] != val:
                nums[i], nums[val - 1] = nums[val - 1], nums[i]
            else:
                i += 1

   
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1