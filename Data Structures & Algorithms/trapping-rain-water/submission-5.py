class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        res = 0

        for i in range(len(height)):
            max_left = max_right = height[i]

            for j in range(i):
                max_left = max(max_left, height[j])
            
            for j in range(i + 1, len(height)):
                max_right =  max(max_right, height[j])

            res += min(max_left , max_right) - height[i]
        return res 


        