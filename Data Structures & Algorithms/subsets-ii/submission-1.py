class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        nums.sort()

        def backtrack(start, path):
            res.append(path[:]) # base case is implicitly true

            for i in range(start, len(nums)):               #sample space of choices
                if i > start and nums[i] == nums[i-1]:      #constraint 
                    continue
                
                path.append(nums[i])                       #make choice
                backtrack(i+1, path)                       
                path.pop()                                 #undo of choice
        

        backtrack(0,path)
        return res
            