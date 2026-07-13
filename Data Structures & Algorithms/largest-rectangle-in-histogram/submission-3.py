class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        heights.append(0)

        for idx, height in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > height:
                pos, hei = stack.pop()
                width = idx - pos
                maxArea = max(maxArea, width * hei)
                start = pos

            stack.append((start, height))
        
        return maxArea
