class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        slow, fast = 0, len(nums) - 1

        while slow < fast:
            currSum = nums[slow] + nums[fast]
            if currSum == target:
                return [slow+1, fast+1]
            elif currSum < target:
                slow += 1
            else:
                fast -= 1
        
        return []
            