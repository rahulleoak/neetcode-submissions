class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        if n == 1:
            return nums[0]

        #adj -> maximum profit considering houses up to i-1
        #far -> maximum profit considering houses up to i-2
        far, adj = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            localRob = max(far + nums[i], adj)

            far = adj
            adj = localRob

        return adj
