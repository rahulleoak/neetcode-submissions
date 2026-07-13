class Solution:
    def valid(self, targetSum, nums, k):
        currSum  = 0
        subArrayCount = 1

        for val in nums:
            if currSum + val > targetSum:
                currSum = val
                subArrayCount += 1

                if subArrayCount > k:
                    return False

            else:
                currSum += val
        
        return subArrayCount <= k

    def splitArray(self, nums: List[int], k: int) -> int:
        self.nums, self.k = nums, k
        low, high = max(nums), sum(nums)

        if len(nums) == k:
            return low
        

        while low <= high:
            mid = low + (high - low) // 2

            if self.valid(mid, nums, k):
                high = mid - 1
            else:
                low = mid + 1

        return low