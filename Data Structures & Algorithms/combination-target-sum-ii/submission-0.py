class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, path = [], []
        candidates.sort()
        n = len(candidates)

        def backtrack(start, currSum):
            if currSum == target:
                res.append(path[::])
                return
            

            for idx in range(start, n):
                val = candidates[idx]

                if currSum + val > target:
                    return
                
                if idx > start and val == candidates[idx-1]:
                    continue
                
                path.append(val)
                backtrack(idx+1, currSum + val)
                path.pop()
            
        backtrack(0,0)
        return res