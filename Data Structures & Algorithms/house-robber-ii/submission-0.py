class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0

        if n == 1:
            return nums[0]
        
        def helper(l, r):
            prev2 = 0
            prev1 = 0

            for i in range(l, r+1):
                curr = max(prev1, prev2 + nums[i])
                prev2, prev1 = prev1, curr
            
            return prev1
        
        return max(helper(0, n-2), helper(1, n-1))

