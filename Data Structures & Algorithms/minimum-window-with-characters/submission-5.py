class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        needWindow = defaultdict(int)
        haveWindow = defaultdict(int)

        for ch in t:
            needWindow[ch] += 1
        
        left = 0
        resIdx = [-1, -1]
        resLen = float('inf')
        have, need  = 0, len(needWindow)

        for right, ch in enumerate(s):
            haveWindow[ch] += 1

            if ch in needWindow and haveWindow[ch] == needWindow[ch]:
                have += 1

            while have == need:
                if (right - left + 1) < resLen:
                    resLen = right - left + 1
                    resIdx = [left, right]
                
                haveWindow[s[left]] -= 1
                if s[left] in needWindow and haveWindow[s[left]] < needWindow[s[left]]:
                    have -= 1
                
                left += 1
        
        leftIdx , rightIdx = resIdx

        return s[leftIdx : rightIdx + 1] if resIdx != [-1,-1] else ""