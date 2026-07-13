class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #(idx, height)
        
        maxArea = 0
        for idx, height in enumerate(heights):
            start = idx
            while stack and height < stack[-1][1]:
                currIdx, currHeight = stack.pop()
                
                width = (idx - currIdx) 
                currArea = currHeight * width

                maxArea = max(maxArea, currArea)
                start =  currIdx

            stack.append((start,height))
        
        for idx, h in stack:
            width = len(heights) - idx
            currArea = h * width
            maxArea = max(maxArea, currArea)

        return maxArea
