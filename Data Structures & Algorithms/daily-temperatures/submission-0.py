class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        
        for idx, t in enumerate(temperatures):
            print(stack)
            while stack and stack[-1][0] < t:
                stackTemp, stackIdx = stack.pop()
                daysDiff = idx - stackIdx
                res[stackIdx] = daysDiff
            stack.append((t,idx))
        
        return res