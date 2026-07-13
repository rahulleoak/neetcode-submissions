class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0 , len(heights) - 1
        globalMax = 0

        while left < right:
            currHeight = min(heights[left], heights[right])
            currWidth = right - left
            currArea = currHeight * currWidth
            globalMax = max(globalMax, currArea)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return globalMax
