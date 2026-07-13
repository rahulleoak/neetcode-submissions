class Solution:
    def trap(self, heights: List[int]) -> int:
        n = len(heights)

        maxLeftHeights = [0] * n
        maxLeftHeights[0] = heights[0]
        for i in range(1,n):
            maxLeftHeights[i] = max(maxLeftHeights[i-1], heights[i])
        
        maxRightHeights = [0] * n
        maxRightHeights[n-1] = heights[n-1]
        for i in range(n-2,-1,-1):
            maxRightHeights[i] = max(maxRightHeights[i+1], heights[i])

        totalArea = 0
        print(maxLeftHeights, maxRightHeights)
        for i in range(n):
            totalArea += min(maxRightHeights[i], maxLeftHeights[i]) - heights[i]

        return totalArea
        