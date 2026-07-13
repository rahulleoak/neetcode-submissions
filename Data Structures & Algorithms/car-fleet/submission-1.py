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
            stack.append(timeToTarget)

            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)