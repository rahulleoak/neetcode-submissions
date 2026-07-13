class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charCount = {}
        
        for c in s:
            charCount[c] = 1 + charCount.get(c,0)
        
        for c in t:
            charCount[c] = charCount.get(c,0) - 1

        for c in s:
            if charCount[c] != 0:
                return False
        
        return True