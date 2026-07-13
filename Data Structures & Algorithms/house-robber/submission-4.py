class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 2:
            return 0 if N == 0 else max(nums)
        

        include, skip = nums[0], max(nums[0], nums[1])

        for i in range(2,N):
            tempMax = max(nums[i] + include , skip)
            include = skip
            skip = tempMax
        
        return skip