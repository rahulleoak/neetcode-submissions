class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charFreq = defaultdict(int)        
        left = 0
        maxFreq = 0
        res = 0

        for right, ch in enumerate(s):
            charFreq[ch] += 1
            maxFreq = max(maxFreq, charFreq[ch])
            width = (right - left + 1)

            while (width - maxFreq) > k:
                charFreq[s[left]] -= 1
                left += 1
                width = right - left + 1
        
            res = max(res, width)
        
        return res

