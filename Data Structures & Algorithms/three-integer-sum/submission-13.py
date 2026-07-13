class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        for idx, val in enumerate(nums):
            if val > 0:
                break
            
            if idx >= 1 and val == nums[idx-1]:
                continue
            
            l, r = idx + 1, len(nums) - 1
            while l < r:
                totalSum = val + nums[l] + nums[r]
                if totalSum == 0:
                    triplets.append([val, nums[l], nums[r]])
                    l += 1 
                    

                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    r -= 1
                elif totalSum > 0:
                    r -= 1
                else:
                    l += 1
        
        return triplets