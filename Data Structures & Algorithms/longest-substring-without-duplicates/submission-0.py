class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        make sure i have unique characters
        make sure that i have some sort of way to keep track of the sequence
        '''


        charSet = set()
        L = 0
        maxLength = 0

        for R, val in enumerate(s):
            while val in charSet:
                charSet.remove(s[L])
                L += 1

            charSet.add(val)
            currWindowLength = R - L + 1
            maxLength = max(maxLength, currWindowLength)
        
        return maxLength
