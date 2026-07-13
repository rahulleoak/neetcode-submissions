class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for idx, val in enumerate(nums):
            
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            if val > 0:
                break
            
            l, r = idx + 1, len(nums) - 1

            while l < r:
                curr = nums[l] + nums[r] + val

                if curr > 0:
                    r -= 1
                elif curr < 0:
                    l += 1
                else:
                    res.append([val, nums[l], nums[r]])
                    l += 1

                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res