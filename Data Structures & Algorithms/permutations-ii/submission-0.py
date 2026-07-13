class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = set()
        
        nums.sort()
        n = len(nums)

        def backtracking(curr):
            if curr == n:
                res.append(path[:])
                return
            
            for idx in range(n):

                if (
                    idx in used or
                    (
                        idx > 0 and
                        nums[idx] == nums[idx - 1] and 
                        (idx-1) not in used
                    )
                ):
                    continue

                used.add(idx)
                path.append(nums[idx])
                
                backtracking(curr+1)
                
                used.remove(idx)
                path.pop()
                
        
        backtracking(0)
        return res