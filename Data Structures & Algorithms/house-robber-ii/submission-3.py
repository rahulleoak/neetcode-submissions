class Solution:
    def simulate(self, subArray):
        if not subArray:
            return 0
        if len(subArray) == 1:
            return subArray[0]
            
        far, adj = subArray[0], max(subArray[0], subArray[1])

        for i in range(2, len(subArray)):
            bestPossible = max(far + subArray[i], adj)

            far = adj
            adj = bestPossible
        
        return adj

    
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        if n == 1:
            return nums[0]
        
        skipFirstHouse = self.simulate(nums[1:])
        skipLastHouse = self.simulate(nums[:-1])

        return max(skipFirstHouse, skipLastHouse)