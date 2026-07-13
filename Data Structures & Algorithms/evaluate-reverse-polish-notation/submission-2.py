class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in "+/*-":
                B = stack.pop()
                A = stack.pop()

                res = 0
                if token == "+":
                    res = A + B
                elif token == "-":
                    res = A - B
                elif token == "*":
                    res = A * B
                else:
                    res = int(A / B)
                
                stack.append(res)
            else:
                stack.append(int(token))
        
        return stack[-1]
