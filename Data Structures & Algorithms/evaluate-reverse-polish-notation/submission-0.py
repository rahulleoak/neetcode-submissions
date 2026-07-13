class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for val in tokens:
            if val not in "+-/*":
                stack.append(int(val))
                continue
            
            n2 = stack.pop()
            n1 = stack.pop()

            res = 0
            if val == "+":
                res = n1 + n2
            elif val == "-":
                res = n1 - n2
            elif val == "*":
                res = n1 * n2
            else:
                res = int(n1/n2)
            
            stack.append(res)
        
        return stack.pop()