class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l = 0
        maxLen = 0

        for r, ch in enumerate(s):
            while ch in window:
                leftChar = s[l]
                window.remove(leftChar)
                l += 1
                


            window.add(ch)
            maxLen = max(maxLen, r-l+1)
            
        return maxLen

