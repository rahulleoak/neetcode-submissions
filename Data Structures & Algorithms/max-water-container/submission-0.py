class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        totalMaxArea = float('-inf')

        while left < right:
            currWidth = right - left
            currHeight = min(heights[left], heights[right])
            currArea = currHeight * currWidth

            totalMaxArea = max(totalMaxArea, currArea)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        

        return totalMaxArea


