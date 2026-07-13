class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = 0

        while l < r:
            width = r - l

            if heights[l] < heights[r]:
                area = heights[l] * width
                if area > maxArea:
                    maxArea = area
                l += 1
            
            else:
                area = heights[r] * width
                if area > maxArea:
                    maxArea = area
                r -= 1
        
        return maxArea
