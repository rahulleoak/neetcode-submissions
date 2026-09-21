class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False


        sDict = defaultdict(int)
        for c in s:
            sDict[c] += 1
        
        for c in t:
            sDict[c] -= 1
            if sDict[c] < 0:
                return False

        return True