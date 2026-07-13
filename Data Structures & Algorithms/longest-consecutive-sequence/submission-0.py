class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        val = set(nums)

        globalMax = 0
        for n in nums:
            if (n - 1) not in val:
                currMax = 1
                while (n+1) in val:
                    currMax += 1
                    n = n+1
                globalMax = max(globalMax, currMax)
        
        return globalMax