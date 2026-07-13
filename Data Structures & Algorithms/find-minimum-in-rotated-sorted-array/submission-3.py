class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo , hi = 0, len(nums) - 1
        res = nums[0]

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            res = min(res, nums[mid])

            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return res