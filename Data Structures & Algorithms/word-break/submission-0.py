class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] *  (n + 1)
        dp[0] = True

        for i in range(n):
            if not dp[i]:
                continue

            for w in wordDict:
                lenOfWord = i + len(w)
                if lenOfWord <= n and s[i: lenOfWord] == w:
                    dp[lenOfWord] = True
        
        return dp[n]