class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        path = []

        def backtrack(start, path):
            res.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
        
        backtrack(0,path)
        return res