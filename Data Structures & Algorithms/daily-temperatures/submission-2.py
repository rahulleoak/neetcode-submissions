class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        '''
        tempreature     = [30, 38, 30, 36, 35, 40, 28]
        temp = [(idx-i, temp-i) ... (idx-n, temp-n)]
        temp            = [(0, 30),  ]
        '''
        
        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                day, _ = stack.pop()
                res[day] = i - day
            stack.append((i,t))
        
        return res