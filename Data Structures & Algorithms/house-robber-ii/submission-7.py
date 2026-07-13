class Solution:
    def simulate(self, nums):
        n = len(nums)
        
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        far = nums[0]
        adj = max(nums[0], nums[1])

        for i in range(2, n):
            maxProfit = max(far + nums[i], adj)

            far = adj
            adj = maxProfit

        return adj

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
            
        skipFirst = self.simulate(nums[1:])
        skipLast = self.simulate(nums[:-1])

        return max(skipFirst, skipLast)