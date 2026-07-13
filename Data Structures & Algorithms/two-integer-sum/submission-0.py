class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compMap = {}

        for idx, val in enumerate(nums):
            complement = target - val
            if complement in compMap:
                return [compMap[complement], idx]
            
            compMap[val] = idx
        
        return []
