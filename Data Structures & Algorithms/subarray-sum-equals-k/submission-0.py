class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0 : 1}
        res = currSum = 0

        for num in nums:
            currSum += num
            difference = currSum - k 

            if difference in prefixSum:
                res += prefixSum[difference]
            
            if currSum not in prefixSum:
                prefixSum[currSum] = 0
            prefixSum[currSum] += 1
        
        return res