class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        twoJump, oneJump  = 1, 2

        for i in range(3, n+1):
            newScore = oneJump + twoJump

            twoJump = oneJump
            oneJump = newScore

        return oneJump