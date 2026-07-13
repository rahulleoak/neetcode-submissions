class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.window = deque()

        self.currSum = 0
        self.population = 0

    def add(self, val):
        n = len(self.window)
        if n == self.size:
            popped  = self.window.popleft()
            self.currSum -= popped
            self.population -= 1
        
        self.window.append(val)
        self.currSum += val
        self.population += 1
    
    def next(self, val: int) -> float:
        self.add(val)

        return self.currSum / min(self.size, self.population)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
