class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        oneCount = 0
        maxCount = 0

        for n in nums:
            if n == 1:
                oneCount += 1  
            else:
                oneCount = 0
            if oneCount > maxCount:
                maxCount = oneCount

        return maxCount
        
