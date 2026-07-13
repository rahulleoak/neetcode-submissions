class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        '''
        tempreature     = [30, 38, 30, 36, 35, 40, 28]
        temp = [(idx-i, temp-i) ... (idx-n, temp-n)]
        temp            = [(0, 30),  ]
        '''
        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                day, _ = stack.pop()
                res[day] = idx - day
            stack.append((idx,temp))
        
        return res