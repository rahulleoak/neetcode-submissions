class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        lenOfNums = len(nums)
        nums.sort()

        # first repr. nums[i]
        for idx, first in enumerate(nums):
            if first > 0:
                break

            # Ensure first is unique for all triplets combinations including it
            if idx > 0 and first == nums[idx-1]:
                continue

            second, third = idx + 1, lenOfNums - 1
            while second < third:
                threeSum = first + nums[second] + nums[third]

                if threeSum > 0:
                    third -= 1
                elif threeSum < 0:
                    second += 1
                else:
                    res.append([first, nums[second], nums[third]])
                    second += 1
                    third -= 1

                    while second < third and nums[second] == nums[second-1]:
                        second += 1
        
        return res

