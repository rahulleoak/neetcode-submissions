class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Len, s2Len = len(s1), len(s2)

        if s1Len > s2Len:
            return False

        s1FreqWindow = [0] * 26
        s2FreqWindow = [0] * 26

        for i in range(s1Len):
            s1FreqWindow[ord(s1[i]) - ord('a')] += 1
            s2FreqWindow[ord(s2[i]) - ord('a')] += 1
        
        if s1FreqWindow == s2FreqWindow:
            return True
        
        left = 0
        for right in range(s1Len, s2Len):
            leftUnicode = ord(s2[left]) - ord('a')
            s2FreqWindow[leftUnicode] -= 1  
            left += 1

            rightUnicode= ord(s2[right]) - ord('a')
            s2FreqWindow[rightUnicode] += 1

            if s1FreqWindow == s2FreqWindow:
                return True
        
        return False