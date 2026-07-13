class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            val = [position[i], speed[i]]
            cars.append(val)
        cars.sort(reverse=True)

        stack = []
        for pos, speed in (cars):
            timeToTarget = (target - pos) / speed
            
            if not stack or stack[-1] < timeToTarget:
                stack.append(timeToTarget)
        return len(stack)