class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lenS1, lenS2 = len(s1), len(s2)

        if lenS1 > lenS2:
            return False

        slidingWindowFreq = [0] * 26
        s1Freq = [0] * 26

        for c in s1:
            s1Freq[ord(c) - ord('a')] += 1
        
        l = 0
        for r, c in enumerate(s2):
            slidingWindowFreq[ord(c) - ord('a')] += 1

            if r >= lenS1:
                slidingWindowFreq[ord(s2[l]) - ord('a')] -= 1
                l += 1
            
            if slidingWindowFreq == s1Freq:
                return True
        
        return False
            