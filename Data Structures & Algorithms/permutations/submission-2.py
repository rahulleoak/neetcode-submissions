class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        def backtrack(start):
            if start == n:
                res.append(nums[:])
                return
            
            for idx in range(start, n):
                nums[start], nums[idx] = nums[idx], nums[start] 
                backtrack(start + 1)
                nums[start], nums[idx] = nums[idx], nums[start]
                #nums[idx], nums[pathLen] = nums[pathLen], nums[idx] 
                
        
        backtrack(0)
        return res

    