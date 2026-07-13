class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0 
        leftB, rightB = 0, len(heights) - 1

        while leftB < rightB:
            if heights[leftB] < heights[rightB]:
                width = rightB - leftB
                area = width * heights[leftB]
                maxWater = max(area, maxWater)
                leftB += 1
            else:
                width = rightB - leftB
                area = width * heights[rightB]
                maxWater = max(area, maxWater)
                rightB -= 1

        return maxWater