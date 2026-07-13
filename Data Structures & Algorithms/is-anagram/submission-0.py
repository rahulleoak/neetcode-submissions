class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charCount = defaultdict(int)

        for c in s:
            charCount[c] += 1
        for c in t:
            charCount[c] -= 1
        
        for val in charCount.values():
            if val != 0:
                return False
        
        return True