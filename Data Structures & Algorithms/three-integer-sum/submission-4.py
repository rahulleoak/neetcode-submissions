class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for idx, val in enumerate(nums):
            if idx > 0 and val == nums[idx - 1]:
                continue
            
            left, right = idx + 1, n-1
            while left < right:
                currSum = val + nums[left] + nums[right] 

                if currSum == 0:
                    res.append([val,nums[left],nums[right]])
                    left += 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                
                elif currSum < 0:
                    left += 1
                else:
                    right -= 1
    
        return res
                    