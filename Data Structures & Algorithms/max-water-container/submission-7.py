class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = float('-inf')
        lenOfHeights = len(heights)
        left, right = 0, lenOfHeights - 1

        while left < right:
            if heights[left] < heights[right]:
                width = right - left
                currArea = width * heights[left]
                maxArea = currArea if currArea > maxArea else maxArea
                left += 1
            else:
                width = right - left
                currArea = width * heights[right]
                maxArea = currArea if currArea > maxArea else maxArea
                right -= 1
        
        return maxArea

