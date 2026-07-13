class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        def backtrack(start, pathLen):
            if pathLen == n:
                res.append(nums[:])
                return
            
            for idx in range(start, n):
                nums[idx], nums[pathLen] = nums[pathLen], nums[idx] 
                backtrack(start + 1, pathLen + 1)
                nums[pathLen], nums[idx] = nums[idx], nums[pathLen]
                #nums[idx], nums[pathLen] = nums[pathLen], nums[idx] 
                
        
        backtrack(0,0)
        return res

    