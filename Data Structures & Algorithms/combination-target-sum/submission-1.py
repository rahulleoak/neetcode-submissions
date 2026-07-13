class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(idx, path):
            if sum(path) == target:
                res.append(path[::])
                return
            
            for i in range(idx, len(nums)):
                if sum(path) + nums[i] > target:
                    continue

                path.append(nums[i])
                dfs(i, path)
                path.pop()
        
        dfs(0,[])
        return res