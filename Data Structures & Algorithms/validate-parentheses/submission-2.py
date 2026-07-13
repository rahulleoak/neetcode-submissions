class Solution:
    def isValid(self, s: str) -> bool:
        pMap = {')':'(','}':'{',']':'['}

        stack = []
        for c in s:
            if c in pMap.values():
                stack.append(c)
            elif c in pMap:
                if not stack or stack.pop() != pMap[c]:
                    return False
        
        return not stack
