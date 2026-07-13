class MinHeap:
    
    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:
        self.heap.append(val)
        idx = len(self.heap) - 1
        self._siftUp(idx)

    def pop(self) -> int:
        length = len(self.heap)
        if length == 1:
            return -1
        elif length == 2: 
            return self.heap.pop()
        
        rootVal = self.heap[1] 
        self.heap[1] = self.heap.pop()
        
        idx = 1
        self._siftDown(idx)
        
        return rootVal
        
    def top(self) -> int:
        length = len(self.heap)
        return self.heap[1] if length > 1 else -1

    def heapify(self, nums: List[int]) -> None:
        self.heap = [0] + nums

        for i in reversed( range( 1, len( self.heap ) // 2 ) ):
            self._siftDown(i)
        
    '''
    Trickle up the tree to see where the value should fit 
    '''
    def _siftUp(self, idx):
        parent = idx // 2
        while (
                idx > 1 and
                self.heap[idx] < self.heap[parent]
        ):  
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            idx = parent
            parent = idx // 2


    '''
    Trickle down the tree to see where the rightmost node (which is now root) should fit in the tree
    '''
    def _siftDown(self, idx):
        length = len(self.heap)
        while 2 * idx < length:
            leftIdx, rightIdx = 2*idx, 2*idx + 1
            smallestIdx = leftIdx                   #Assume left is smaller
            if (
                rightIdx < length and
                self.heap[rightIdx] < self.heap[leftIdx]    
            ): #Check to see if right is smallest and also make sure new rightIdx is within bounds
                smallestIdx = rightIdx #IF true, right is now smaller
            
            if self.heap[idx] > self.heap[smallestIdx]:
                #See if currentIdx value is larger than the value at the smallestIdx, if so swap
                self.heap[idx], self.heap[smallestIdx] = self.heap[smallestIdx], self.heap[idx]
                idx = smallestIdx
            else:
                break #Avoids infinite cycle
        
        