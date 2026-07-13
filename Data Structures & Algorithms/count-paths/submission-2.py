class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevState = [1] * (n)
        
        for r in range(1, m):
            currState = [1] * (n)
            for c in range(1, n):
                currState[c] = prevState[c] + currState[c-1]
            
            prevState = currState
        
        return prevState[n-1]
                