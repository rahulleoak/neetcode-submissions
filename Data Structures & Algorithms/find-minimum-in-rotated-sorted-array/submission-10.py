class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:           
            m = (l + r) // 2
            res = min(res, nums[m])

            if nums[m] < nums[r]:
                r = m
            else:
                l  = m + 1

        return res