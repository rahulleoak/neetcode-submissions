class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        needWindow = {}
        for ch in t:
            if ch not in needWindow:
                needWindow[ch] = 1
            else:
                needWindow[ch] += 1
        

        haveWindow = {}
        left = 0
        windowIdx = [-1, -1]
        minLen = float('inf')
        have, need = 0, len(needWindow)

        for right, ch in enumerate(s):
            if ch not in haveWindow:
                haveWindow[ch] = 1
            else:
                haveWindow[ch] += 1

            if ch in needWindow and haveWindow[ch] == needWindow[ch]:
                have += 1
            
            while have == need:
                if (right - left + 1) < minLen:
                    minLen = right - left + 1
                    windowIdx = [left, right]

                haveWindow[s[left]] -= 1
                if s[left] in needWindow and haveWindow[s[left]] < needWindow[s[left]]:
                    have -= 1
                left += 1
        
        leftIdx, rightIdx = windowIdx

        return s[leftIdx : rightIdx + 1] if minLen != float('inf') else ""
                   