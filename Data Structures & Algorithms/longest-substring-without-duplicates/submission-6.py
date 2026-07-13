class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0

        uniqueChar = set()
        left = 0
        maxLenOfSS = 0
            
        for right, char in enumerate(s):
            while char in uniqueChar:
                uniqueChar.remove(s[left])
                left += 1

            uniqueChar.add(char)
            currLenOfSS = right - left + 1
            maxLenOfSS = max(maxLenOfSS, currLenOfSS)

        return maxLenOfSS
