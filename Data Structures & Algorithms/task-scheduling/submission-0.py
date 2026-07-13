class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqMap = defaultdict(int)
        for task in tasks:
            freqMap[task] += 1
        
        maxHeap = [-x for x in freqMap.values()]
        heapq.heapify(maxHeap)
        cooldown = deque()

        time = 0 
        while maxHeap or cooldown:
            time += 1

            if maxHeap:
                currFreq = -heapq.heappop(maxHeap)
                if currFreq > 1:
                    newEntry = (currFreq - 1, time + n)
                    cooldown.append(newEntry)
            
            while cooldown and cooldown[0][1] == time:
                freq, _ = cooldown.popleft()
                heapq.heappush(maxHeap, -freq)
        
        return time