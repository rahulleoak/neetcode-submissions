class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        freqCount = defaultdict(int)

        for i in range(len(s)):
            freqCount[s[i]] += 1
            freqCount[t[i]] -= 1

        
        for val in freqCount.values():
            if val != 0:
                return False
        return True
        