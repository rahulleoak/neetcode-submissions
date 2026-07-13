class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (startIdx, height)
        maxArea = 0
        heights.append(0) # ensure all bars in stack are processed

        for idx, height in enumerate(heights):
            start = idx # represents how far back the height can cover
            # if curr height is smaller than top, we can no longer extend the prev. taller bars
            while stack and stack[-1][1] > height:
                pos, hei = stack.pop()
                width = idx - pos
                maxArea = max(maxArea, width * hei)
                
                # Current shorter bar can actually start from popped bar position
                start = pos

            stack.append((start, height))
        
        return maxArea
