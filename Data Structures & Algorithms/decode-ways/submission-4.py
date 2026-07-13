class Solution:
    def numDecodings(self, s: str) -> int:
        if not(s) or s[0] == "0":
            return 0
        
        n = len(s) 
        dp = [0] * (n+1)
        
        # Empty String, weird but the number of ways to potenially guess 's'
        dp[0] = 1 
        dp[1] = 1 # WE already checked if s[0] != 0
        
        for i in range(2, n+1):
            # Verify is s[i] can be a valid digit
            # ex: "2" is valid and "0" is never valid
            if s[i-1] != "0":
                dp[i] += dp[i-1] 


            # Verify if s[i-2:i] is valid digit
            # ex: "12" is valid since its within 10 and 26, 
            #      otherwise we can't represent the char numerically
            if "10" <= s[i-2:i] <= "26":
                dp[i] += dp[i-2]
        
        return dp[-1]
        