class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0 , len(height) - 1
        leftMax, rightMax = height[left], height[right]
        waterContent = 0

        while left < right:
            # Proccess left side
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                waterContent += leftMax - height[left]

            # Process right side
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                waterContent += rightMax - height[right]
        
        return waterContent
