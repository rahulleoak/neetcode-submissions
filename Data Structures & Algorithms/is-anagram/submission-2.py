class Solution:
    def isAnagram(self, s: str, t: str) -> bool: 
        charMap = defaultdict(int)

        for c in s:
            charMap[c] += 1
        
        for c in t:
            charMap[c] -= 1
        

        for val in charMap.values():
            if val != 0:
                return False
        
        return True