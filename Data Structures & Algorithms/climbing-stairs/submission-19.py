class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        twoJump, oneJump  = 1, 2

        for i in range(3, n+1):
            twoJump, oneJump = oneJump, oneJump + twoJump

        return oneJump