class MedianFinder:

    def __init__(self):
        self.smallVals = [] # maxheap
        self.largeVals = [] # minheap

    def addNum(self, num: int) -> None:
        if self.largeVals and num > self.largeVals[0]:
            heapq.heappush(self.largeVals, num)
        else:
            heapq.heappush(self.smallVals, -num)
        
        if len(self.largeVals) > 1 + len(self.smallVals):
            val = heapq.heappop(self.largeVals)
            heapq.heappush(self.smallVals, -val)
        if len(self.smallVals) > 1 + len(self.largeVals):
            val = -heapq.heappop(self.smallVals)
            heapq.heappush(self.largeVals, val)
            
    def findMedian(self) -> float:
        if len(self.smallVals) > len(self.largeVals):
            return -self.smallVals[0]
        elif len(self.largeVals) > len(self.smallVals):
            return self.largeVals[0]
        
        oddMedian = (self.largeVals[0] + -self.smallVals[0]) / 2.0
        return oddMedian
        