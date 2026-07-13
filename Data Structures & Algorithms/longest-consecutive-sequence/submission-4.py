class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        unique = set(nums)
        maxLen = float('-inf')

        for val in nums:
            if val - 1 not in unique:
                length = 1
                while val + length in unique:
                    length += 1

                maxLen = max(maxLen, length)

        return maxLen