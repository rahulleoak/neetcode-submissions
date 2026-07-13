class Solution:
    def findPalindrome(self, l, r, maxLen, s):
        resIdx = [0, 0]
        while l >= 0 and r < len(s) and s[l] == s[r]:
            currLen = r - l + 1
            if currLen > maxLen:
                resIdx = [l, r]
                maxLen = r - l + 1
            l -= 1
            r += 1
        return resIdx, maxLen

    def longestPalindrome(self, s: str) -> str:
        resIdx = [0, 0]
        maxLen = float('-inf')

        for i in range(len(s)):
            # odd
            l = r = i
            currIdx, currLen = self.findPalindrome(l, r, maxLen, s)
            if currLen > maxLen:
                resIdx = currIdx
                maxLen = currLen

            # even
            l, r = i , i + 1
            currIdx, currLen = self.findPalindrome(l, r, maxLen, s)
            if currLen > maxLen:
                resIdx = currIdx
                maxLen = currLen

        l, r = resIdx
        return s[l : r+1]