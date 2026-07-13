class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charCounter = {}
        
        for ch in s:
            if ch not in charCounter:
                charCounter[ch] = 0
            charCounter[ch] += 1
        
        for ch in t:
            if ch not in charCounter:
                return False
            charCounter[ch] -= 1
            if charCounter[ch] == 0:
                del charCounter[ch]
        
        return not charCounter
