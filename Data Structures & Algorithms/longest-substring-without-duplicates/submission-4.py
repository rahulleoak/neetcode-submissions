class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniqueChar = set()  
        left = 0
        maxLen = 0

        for right, val in enumerate(s):
            while val in uniqueChar:
                uniqueChar.remove(s[left])
                left += 1
            uniqueChar.add(val)
            currLen = right - left + 1
            maxLen = max(maxLen, currLen)
        
        return maxLen

