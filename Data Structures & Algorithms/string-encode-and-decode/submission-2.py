class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            res += str(len(word)) + "#" + word
        
        return res
        
    def decode(self, s: str) -> List[str]:
        res = []

        curr = 0
        while curr < len(s):
            fast = curr
            while s[fast] != "#":
                fast += 1
            
            lenOfWord = int(s[curr:fast])
            curr = fast + 1
            fast = curr + lenOfWord
            
            res.append(s[curr:fast])

            curr = fast

        return res

