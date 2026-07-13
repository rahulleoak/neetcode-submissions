class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        minLen = float('inf')
        totalSum = 0

        for r, val in enumerate(nums):
            totalSum += val

            while totalSum >= target:
                minLen = min(minLen, r - l +1)
                totalSum -= nums[l]
                l += 1

                

        return minLen if minLen != float('inf') else 0