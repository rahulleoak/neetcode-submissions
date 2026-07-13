class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        m, n = len(s1), len(s2)

        # dp[i][j] means s1[:i] and s2[:j] can form s3[:i+j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        dp[0][0] = True
        
        for i in range(1, m + 1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                # Curr s3 is s3[i + j - 1]
                fromS1 = dp[i-1][j] and s1[i-1] == s3[i+j-1]
                fromS2 = dp[i][j-1] and s2[j-1] == s3[i+j-1]

                dp[i][j] = fromS1 or fromS2

        return dp[m][n]