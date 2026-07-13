class Solution:
    def simulate(self, nums, start, end):
        length = end - start + 1
        if length == 0: return 0
        if length == 1: return nums[start]
            
        far, adj = nums[start], max(nums[start], nums[start+1])

        for i in range(start+2, end+1):
            bestPossible = max(far + nums[i], adj)

            far = adj
            adj = bestPossible
        
        return adj

    
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        if n == 1:
            return nums[0]
        
        skipFirstHouse = self.simulate(nums, 1, n-1)
        skipLastHouse = self.simulate(nums, 0, n-2)

        return max(skipFirstHouse, skipLastHouse)