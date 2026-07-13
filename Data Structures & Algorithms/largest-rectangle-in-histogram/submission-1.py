class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #(stackWidth, stackHeight)
        heights.append(-1)
        maxArea = 0 

        for h in heights:
            step = 0
            while stack and stack[-1][1] >= h:
                stackW, stackH = stack.pop()
                step += stackW
                maxArea = max(maxArea, step * stackH)
            
            stack.append((step+1, h))

        return maxArea