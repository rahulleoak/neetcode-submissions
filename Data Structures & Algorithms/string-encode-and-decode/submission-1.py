class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        curr = 0
        while curr < len(s):
            fast = curr
            while s[fast] != "#":
                fast += 1
            
            length = int(s[curr:fast])
            curr = fast + 1
            fast = curr + length
            res.append(s[curr:fast])

            curr = fast
        
        return res

