import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(left,right,lowerBound):
            idx = -1

            while left <= right:
                mid = left + (right - left) // 2
                value = nums[mid]

                if value < target:
                    left = mid + 1
                elif value > target:
                    right = mid - 1
                else:
                    idx = mid

                    if lowerBound:
                        right = mid - 1
                    else:
                        left = mid + 1
            return idx

        left, right = 0, len(nums) - 1
        
        lower = binarySearch(left, right, True)
        upper = binarySearch(left, right, False)

        return [lower, upper]