class Solution:
    def middleOutExpansion(self, l, r, s):
        matches = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            matches += 1
        
        return matches
    
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            # odd even palindromes
            l = r = i
            count += self.middleOutExpansion(l,r,s)    

            # even length palindromes
            l, r = i, i+1
            count += self.middleOutExpansion(l,r,s)

        
        return count