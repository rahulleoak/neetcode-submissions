class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for idx, val in enumerate(nums):
            l, r = idx + 1, len(nums) - 1
            
            if val > 0:
                break
            
            if idx > 0 and val == nums[idx - 1]:
                continue

            while l < r:
                currSum = val + nums[l] + nums[r]

                if currSum == 0:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l-1] == nums[l]:
                        l += 1

                elif currSum > 0:
                    r -= 1
                else:
                    l += 1
        
        return res