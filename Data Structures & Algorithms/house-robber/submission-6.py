class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        
        def dfs(i):
            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]

            memo[i] = max(dfs(i+1), nums[i] + dfs(i+2))

            return memo[i]
        
        return dfs(0)




        # if not nums: return 0
        # if len(nums) == 1: return nums[0]
        
        # take, skip = nums[0], 0

        # for i in range(1, len(nums)):
        #     new_take = skip + nums[i]
        #     new_skip = max(take, skip)
        #     take, skip = new_take, new_skip

        # return max(take, skip)