class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [nums[0]]
        for i in range(1,n):
            val = prefix[i-1] * nums[i]
            prefix.append(val)
        
        suffix = [1] * n
        suffix[-1] = nums[-1]
        for i in range(n-2,-1,-1):
            val = suffix[i+1] * nums[i]
            suffix[i] = val
        
        res = []
        for i in range(n):
            if i == 0:
                res.append(suffix[i+1])
            elif i == (n-1):
                res.append(prefix[i-1])
            else:
                val = prefix[i-1] * suffix[i+1]
                res.append(val)
        
        return res