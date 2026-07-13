class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = {}

        def helper(currIdx):
            if currIdx == n:
                return 1
            if s[currIdx] == "0":
                return 0
            if currIdx in memo:
                return memo[currIdx]
            res = helper(currIdx + 1)
            
            if (
                currIdx < n and
                10 <= int(s[currIdx:currIdx+2]) <= 26
            ):
                res += helper(currIdx + 2)

            memo[currIdx] = res
            return memo[currIdx]
        
        return helper(0)