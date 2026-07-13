class Solution:
    def isPalindrom(self, l, r):
        while l <= r:
            if self.s[l] != self.s[r]:
                return False
            l += 1
            r -= 1

        return True
    
    
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        self.s = s

        while l <= r:
            if s[l] != s[r]:
                return (self.isPalindrom(l+1, r) or self.isPalindrom(l, r-1))
            l += 1
            r -= 1

        return True
