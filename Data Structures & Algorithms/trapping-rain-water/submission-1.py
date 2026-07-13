class Solution:
    def trap(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maxL, maxR = heights[0], heights[-1]
        totalArea = 0

        while left < right:
            if maxL <= maxR:
                left += 1
                maxL = max(maxL, heights[left])
                totalArea += maxL - heights[left]
            else:
                right -= 1
                maxR = max(maxR, heights[right])
                totalArea += maxR - heights[right]
        
        return totalArea
        