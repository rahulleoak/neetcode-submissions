class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementMap = {}

        for idx, val in enumerate(nums):
            complement = target - val

            if complement in complementMap:
                complementIdx = complementMap[complement]
                return [complementIdx, idx]
            else:
                complementMap[val] = idx
        
