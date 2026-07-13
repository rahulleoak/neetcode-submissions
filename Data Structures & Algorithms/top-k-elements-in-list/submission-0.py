import heapq as hq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = defaultdict(int)
        for n in nums:
            freqMap[n] += 1
        
        
        minHeap = []
        for key in freqMap.keys():
            if len(minHeap) == k:
                hq.heappushpop(minHeap, (freqMap[key], key))
            else:
                hq.heappush(minHeap, (freqMap[key], key))

        res = []
        for x in minHeap:
            val = x[1]
            res.append(val)
        
        return res