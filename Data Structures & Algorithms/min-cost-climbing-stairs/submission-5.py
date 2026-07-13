class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        # From the floor, i can either go to the first (0-idx) step or second (1-idx) step
        # aka: From step i, i can come from i-1 (oneJump) or i-2 (twoJump)
        oneJump, twoJump = cost[0], 0

        for i in range(1, n):
            ans = min(oneJump, twoJump) + cost[i]

            # For i -> i+1 : the new twoJump will be the old oneJump since the new twoJump is (i+1) - 2 
            twoJump = oneJump
            # For i -> i+1: oneJump should represent i-1, which is what we calculcated and what i+1 will use for i-1 step jump
            oneJump = ans
        
        return min(oneJump, twoJump)
        '''
        n = len(cost)

        for i in range(2, n):
            cost[i] += min(cost[i-1], cost[i-2])
        
        return min(cost[-1], cost[-2])
        '''