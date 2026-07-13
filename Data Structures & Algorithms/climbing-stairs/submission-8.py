class Solution:
    def __init__(self):
        self.n = 0
    def backtrack (self, curr):
        if curr == self.n:
            return 1
        if curr > self.n:
            return 0
        
        return self.backtrack(curr+1) + self.backtrack(curr+2)
        
    def climbStairs(self, n: int) -> int:
        self.n = n
        return self.backtrack(0)