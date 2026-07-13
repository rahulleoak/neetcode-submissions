class Solution:
    def maxArea(self, heights: List[int]) -> int:
        x1, x2 = 0, len(heights) - 1
        maxArea = 0

        while x1 < x2:
            width = x2 - x1

            if heights[x1] < heights[x2]:
                maxArea = max(maxArea, width * heights[x1])
                x1 += 1
            else:
                maxArea = max(maxArea, width * heights[x2])
                x2 -= 1
        
        return maxArea