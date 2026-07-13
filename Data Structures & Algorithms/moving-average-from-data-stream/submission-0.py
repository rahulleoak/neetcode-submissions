class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.window = deque()

    def add(self, val):
        if len(self.window) == self.size:
            self.window.popleft()
        
        self.window.append(val)
    
    def next(self, val: int) -> float:
        self.add(val)

        return sum(self.window) / len(self.window)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
