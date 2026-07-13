class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(index, path, currSum):
            if currSum == target:
                res.append(path[:])
                return
            

            for i in range(index, len(nums)):
                if currSum + nums[i] > target:
                    break

                path.append(nums[i])
                backtrack(i, path, currSum+nums[i])
                path.pop()
            
        backtrack(0, [], 0)
        return res
