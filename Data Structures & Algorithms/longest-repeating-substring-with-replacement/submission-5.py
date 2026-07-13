class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Characters that arent the most freq would need to be replaced
        chFreq = collections.defaultdict(int)
        maxFreq = 0
        l = 0
        validWindowLen = 0
        
        for r, ch in enumerate(s):
            chFreq[ch] += 1
            maxFreq = max(maxFreq, chFreq[ch])

            # Window is VALID as long as: windowSize - count of the most freq ch (so far) <= k    
            #   If i remove the all occurences of the most freq char, how many char remain?
            while k < ((r - l + 1) - maxFreq):
                chFreq[s[l]] -= 1
                l += 1           

            validWindowLen = max(validWindowLen, r - l + 1)

        return validWindowLen