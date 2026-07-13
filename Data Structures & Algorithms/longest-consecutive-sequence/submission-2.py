class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        
        maxLen = 0

        for val in nums:
            if val - 1 not in unique:
                length = 1
                while val + length in unique:
                    length += 1
                if length > maxLen:
                    maxLen = length

        return maxLen