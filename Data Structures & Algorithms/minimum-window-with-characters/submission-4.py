class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sLen, tLen = len(s), len(t)

        if tLen > sLen:
            return ""
        
        needWindow = defaultdict(int)
        haveWindow = defaultdict(int)

        for c in t:
            needWindow[c] += 1

        resLen = float('inf')
        resIdx = [-1, -1]
        left = 0
        have, need = 0, len(needWindow)

        for right, c in enumerate(s):
            haveWindow[c] += 1

            if c in needWindow and haveWindow[c] == needWindow[c]:
                have += 1
            
            while have == need:
                if (right - left + 1) < resLen:
                    resLen = right - left + 1
                    resIdx = [left, right]
                
                haveWindow[s[left]] -= 1

                if s[left] in needWindow and haveWindow[s[left]] < needWindow[s[left]]:
                    have -= 1
                left += 1
        
        leftIdx, rightIdx = resIdx

        return s[leftIdx:rightIdx + 1] if resLen != float('inf') else ""

