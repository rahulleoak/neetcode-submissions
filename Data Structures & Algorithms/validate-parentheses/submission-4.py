class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesesMap ={
            ")":"(",
            "}":"{",
            "]":"["
        }

        for ch in s:
            if ch in parenthesesMap:
                if not stack or parenthesesMap[ch] != stack.pop():
                    return False
            else:
                stack.append(ch)
        
        return not stack