class Solution:
    def palindromeCount(self, l, r, s):
        n = len(s)

        palindromeCount = 0
        while l >= 0 and r < n and s[l] == s[r]:
            palindromeCount += 1
            l -= 1
            r += 1
        
        return palindromeCount

    def countSubstrings(self, s: str) -> int:
        '''
        Fix a center
        Expand outwards as long as characters match
        Each successful expansion forms one palindrome
        '''
        
        totalPalindromeCount = 0


        for idx in range(len(s)):
            # odd len
            totalPalindromeCount += self.palindromeCount(idx,idx,s)

            # even len
            totalPalindromeCount += self.palindromeCount(idx,idx+1,s)
        
        return totalPalindromeCount