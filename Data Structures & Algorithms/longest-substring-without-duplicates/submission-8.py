class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        l = 0 
        maxWindowSize = 0

        for r, ch in enumerate(s):
            if ch in window:
                l = max(window[ch] + 1, l)
            
            window[ch] = r

            if r - l + 1 > maxWindowSize:
                maxWindowSize = r - l + 1
        
        return maxWindowSize
        