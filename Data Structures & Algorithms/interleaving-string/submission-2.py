class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        m, n = len(s1), len(s2)

        # dp[i][j] means s1[:i] and s2[:j] can form s3[:i+j]
        dp = [False] * (n + 1)
        
        dp[0] = True # Empty s1 and s2 form empty s3
        # Prefill first row  (where we only use chars from s2)
        for j in range(1, n + 1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]

        for i in range(1, len(s1) + 1):
            dp[0] = dp[0] and s1[i-1] == s3[i-1]
            possible = dp[0]
            for j in range(1, len(s2) + 1):
                # Curr s3 is s3[i + j - 1]

                # dp[j] (prevRow) represents using s1[i-1]
                fromS1 = dp[j] and s1[i-1] == s3[i+j-1]
                # dp[j-1] (currRow) represents using s2[j-1]
                fromS2 = dp[j-1] and s2[j-1] == s3[i+j-1]

                dp[j] = fromS1 or fromS2
                if dp[j]: possible = True

            if not possible: return False

        return dp[n]