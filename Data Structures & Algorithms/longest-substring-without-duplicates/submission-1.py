class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        L = 0
        maxSubstringLen = 0

        for R, val in enumerate(s):
            while val in charSet:
                charSet.remove(s[L])
                L += 1
            
            charSet.add(val)
            currSubstringLen = R - L + 1
            maxSubstringLen = max(maxSubstringLen, currSubstringLen)

        return maxSubstringLen



