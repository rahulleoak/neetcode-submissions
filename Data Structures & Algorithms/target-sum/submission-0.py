class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = defaultdict(int)

        def dfs(idx, currSum):
            if idx == len(nums):
                return 1 if currSum == target else 0
            if (idx, currSum) in memo:
                return memo[(idx,currSum)]

            memo[(idx, currSum)] += dfs(idx+1, nums[idx] + currSum)
            memo[(idx, currSum)] += dfs(idx+1, (-1 * nums[idx]) + currSum)

            return memo[(idx, currSum)]

            
        return dfs(0,0)
