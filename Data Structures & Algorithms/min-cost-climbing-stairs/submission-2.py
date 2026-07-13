class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        for i in range(2, n):
            cost[i] += min(cost[i-1], cost[i-2])
        
        return min(cost[-1], cost[-2])

        # # From the floor, i can either go to the first (0-idx) step or second (1-idx) step
        # oneJump, twoJump = cost[0], cost[1]

        # for i in range(2, n):
        #     oneJump, twoJump = twoJump, min(oneJump, twoJump) + cost[i]

        # return min(oneJump, twoJump)
