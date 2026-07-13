class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        if m < n:
            s1, s2 = s2, s1
            m, n = n, m
           
        # dp[i][j] means s1[:i] and s2[:j] can form s3[:i+j]
        prevState = [False] * (n + 1)
        
        prevState[0] = True # Empty string (s2) forms empty s3
        # Prefill first row  (where we only use chars from s2)
        for j in range(1, n + 1):
            prevState[j] = prevState[j-1] and s2[j-1] == s3[j-1]

        for i in range(1, m+1):
            prevState[0] = prevState[0] and s1[i-1] == s3[i-1]
            possible = prevState[0]
            for j in range(1, n+1):
                # Curr s3 is s3[i + j - 1]

                # dp[j] (prevRow) represents using s1[i-1]
                fromS1 = prevState[j] and s1[i-1] == s3[i+j-1]
                # dp[j-1] (currRow) represents using s2[j-1]
                fromS2 = prevState[j-1] and s2[j-1] == s3[i+j-1]

                prevState[j] = fromS1 or fromS2
                if prevState[j]: possible = True

            if not possible: return False

        return prevState[n]