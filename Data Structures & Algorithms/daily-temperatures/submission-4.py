class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        daysTillWarmer = [0] * n
        monoStack = []

        for idx, t in enumerate(temperatures):
            # Stack holds all days/temperatures WAITING for a warmer day
            while monoStack and monoStack[-1][1] < t:
                prevDay, prevTemp = monoStack.pop()
                daysToWait = idx - prevDay
                daysTillWarmer[prevDay] = daysToWait

            monoStack.append((idx, t))
        
        return daysTillWarmer