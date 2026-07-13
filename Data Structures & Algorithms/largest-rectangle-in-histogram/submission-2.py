class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(-1)
        maxArea = 0

        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                currHeight = heights[stack.pop()]
                width = i - stack[-1] - 1 if stack else i
                maxArea = max(maxArea, currHeight * width)
            stack.append(i)
        
        return maxArea
