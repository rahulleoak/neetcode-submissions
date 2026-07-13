class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsetSum = []

        def dfs(idx, currXOR):
            if idx == len(nums):
                subsetSum.append(currXOR)
                return
            
            pick = dfs(idx+1, currXOR ^ nums[idx])
            skip = dfs(idx+1, currXOR)

        
        dfs(0,0)
        return sum(subsetSum)