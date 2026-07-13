class Solution:
    def __init__(self):
        self.memo = None
        self.n = 0
    def backtrack (self, curr):
        if curr == self.n:
            return 1
        if curr > self.n:
            return 0
        
        if self.memo[curr] > 0:
            return self.memo[curr]
        self.memo[curr] =  self.backtrack(curr+1) + self.backtrack(curr+2)

        return self.memo[curr]

    def climbStairs(self, n: int) -> int:
        self.memo = [0] * (n+1)
        self.n = n
        return self.backtrack(0)