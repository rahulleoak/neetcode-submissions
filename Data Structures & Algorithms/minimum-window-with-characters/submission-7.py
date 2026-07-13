class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needWindow = defaultdict(int)
        for ch in t:
            needWindow[ch] += 1
        
        left, minLen = 0, float('inf')
        window = [0,0] # Store the min window idx
        haveWindow = defaultdict(int)
        have, need = 0, len(needWindow) # Have nothing in the beginning

        for right, ch in enumerate(s):
            haveWindow[ch] += 1

            if haveWindow[ch] == needWindow[ch]:
                have += 1

            while have == need:
                if minLen > (right - left +1):
                    window = [left, right]
                    minLen = right - left + 1
                
                haveWindow[s[left]] -= 1
                if haveWindow[s[left]] < needWindow[s[left]]:
                    have -= 1
                
                left += 1
        
        start, end = window
        return s[start : end+1] if minLen != float('inf') else ""
                     