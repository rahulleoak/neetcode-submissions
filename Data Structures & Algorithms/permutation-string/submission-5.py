class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        windowSize = len(s1)
        
        s1CharMap = [0] * 26
        window = [0] * 26 # basically s2CharMap
        for idx in range(windowSize):
            s1CharMap[ord(s1[idx]) - ord('a')] += 1
            window[ord(s2[idx]) - ord('a')] += 1
        
        if window == s1CharMap:
            return True

        # matches = 0
        # for i in range(26):
        #     if s1CharMap[i] == window[i]:
        #         matches += 1
        
        
        left = 0
        for right in range(windowSize, len(s2)):
            rightIndex = ord(s2[right]) - ord('a')
            window[rightIndex] += 1

            leftIndex = ord(s2[left]) - ord('a')
            window[leftIndex] -= 1
            left += 1

            if window == s1CharMap:
                return True


        return window == s1CharMap
