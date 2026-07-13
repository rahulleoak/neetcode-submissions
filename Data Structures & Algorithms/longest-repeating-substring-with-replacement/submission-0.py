class Solution:
    def characterReplacement(self, s: str, k: int) -> int: 
        charCounter = defaultdict(int)

        L = 0
        maxFreq = 0
        res = 0

        for R, val in enumerate(s):
            charCounter[val] += 1
            maxFreq = max(maxFreq, charCounter[val])

            width = R - L + 1
            while (width - maxFreq) > k:
                charCounter[s[L]] -= 1
                L += 1
                width = R - L + 1
            
            res = max(res, width)
        
        return res


        

    

         