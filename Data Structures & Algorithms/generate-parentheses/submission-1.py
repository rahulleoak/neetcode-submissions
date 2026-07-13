class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        
        def backtracking(openCount, closeCount, n):
            if openCount == closeCount == n:
                res.append("".join(path))
                return
            
            if openCount < n:
                path.append("(")
                backtracking(openCount+1, closeCount, n)
                path.pop()
            
            if closeCount < openCount:
                path.append(")")
                backtracking(openCount, closeCount+1, n)
                path.pop()
        
        res = []
        path = []

        backtracking(0,0,n)
        return res