class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        operations = ["+", "-", "/", "*"]
        valid = set(operations)

        for t in tokens:
            if t not in operations:
                stack.append(int(t))
            else:
                valB = stack.pop()
                valA = stack.pop()
                
                res = 0
                if t == "+":
                    res = valA + valB
                elif t == "-":
                    res = valA - valB
                elif t == "*":
                    res = valA * valB
                else: # /
                    res = int(valA / valB)
                
                stack.append(res)
        
        return stack.pop()

