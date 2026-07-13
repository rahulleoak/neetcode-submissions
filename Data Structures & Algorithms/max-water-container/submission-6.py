class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maxArea = 0

        while left < right:
            if heights[left] < heights[right]:
                width = right - left
                currArea = heights[left] * width
                maxArea = max(maxArea, currArea)
                left += 1
            else:
                width = right - left
                currArea = heights[right] * width
                maxArea = max(maxArea, currArea)
                right -= 1
        
        return maxArea