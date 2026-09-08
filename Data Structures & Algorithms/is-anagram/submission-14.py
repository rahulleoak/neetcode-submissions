class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charMap = defaultdict(int)

        for c in s:
            charMap[c] += 1
        
        for c in t:
            charMap[c] -= 1
            if charMap[c] < 0:
                return False
        
        return True