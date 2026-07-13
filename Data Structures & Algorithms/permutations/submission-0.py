class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(index):
            if index == len(nums):                              #Base Case
                res.append(nums[:])
                return
            
            for i in range(index, len(nums)):                   #Exploring our samples/chocies
                nums[index] , nums[i] = nums[i], nums[index]    #Making a choice
                backtrack(index+1)                              #Backtracking Step
                nums[index] , nums[i] = nums[i], nums[index]    #Undo Choice

        res = []
        backtrack(0)
        return res
            