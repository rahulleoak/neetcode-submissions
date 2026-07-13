class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = element = 0

        for n in nums:
            if count == 0:
                element = n
                count = 1
            elif n == element:
                count += 1
            else:
                count -= 1
        
        return element