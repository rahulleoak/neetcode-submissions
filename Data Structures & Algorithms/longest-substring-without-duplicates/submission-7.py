class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l = 0 
        maxWindowSize = 0

        for r, ch in enumerate(s):
            while ch in window:
                window.remove(s[l])
                l += 1
            
            window.add(ch)
            
            if r - l + 1 > maxWindowSize:
                maxWindowSize = r - l + 1
        
        return maxWindowSize
        