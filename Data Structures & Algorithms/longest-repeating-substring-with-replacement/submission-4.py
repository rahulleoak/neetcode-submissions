class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        freqMap = defaultdict(int)
        res = maxFreq = maxWindow = 0

        for r in range(len(s)):
            freqMap[s[r]] += 1
            maxFreq = max(maxFreq, freqMap[s[r]])
            width = r - l + 1

            if width - maxFreq > k:
                freqMap[s[l]] -= 1
                l += 1

                width = r - l + 1
            
            res = max(width, res)
        
        return res
            