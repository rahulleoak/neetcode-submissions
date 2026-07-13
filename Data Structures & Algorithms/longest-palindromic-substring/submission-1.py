class Solution:
    def isPalindrome(self, s, l, r, maxLen):
        n = len(s)
        resIdx = [l, r]
        while l >= 0 and r < n and s[l] == s[r]:
            if (r - l + 1) > maxLen:
                maxLen = r - l + 1
                resIdx = [l, r]
            
            l -= 1
            r += 1
        
        return resIdx, maxLen
   

    def longestPalindrome(self, s: str) -> str:
        maxLen = float('-inf')
        resIdx = [0, 0]

        # Idea: Expand from center

        for idx in range(len(s)):
            # odd length palindromes
            l = r = idx
            oddIdx, oddLen = self.isPalindrome(s,l,r,maxLen)
            if oddLen > maxLen:
                maxLen = oddLen
                resIdx = oddIdx

            # even length palindromes
            l, r = idx, idx +1
            evenIdx, evenLen = self.isPalindrome(s,l,r,maxLen)
            if evenLen > maxLen:
                maxLen = evenLen
                resIdx = evenIdx
        
        l , r = resIdx
        return s[l:r+1]
        
