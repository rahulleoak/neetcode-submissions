class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0

        if n == 1:
            return nums[0]

        return max(self.simulate(nums[1:]), self.simulate(nums[:-1]))

    def simulate (self, subArray):
        take, skip = subArray[0], 0

        for i in range(1, len(subArray)):
            newTake = skip + subArray[i]
            newSkip = max(take, skip)

            take, skip = newTake, newSkip
        
        return max(take, skip)