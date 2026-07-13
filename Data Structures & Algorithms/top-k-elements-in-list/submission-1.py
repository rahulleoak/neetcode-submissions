import heapq as hq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # assign heap and counter
        heap, counter = [], {}

        # populate counter
        for num in nums:
            if num not in counter:
                counter[num] = 0    
            counter[num] += 1

        # populate heap
        for num, freq in counter.items():
            hq.heappush(heap, (freq, num))

            if len(heap) > k:
                hq.heappop(heap)

        # populate final result list
        res = []
        while heap:
            res.append(hq.heappop(heap)[1])

            if len(res) == k:
                return res
        

        
        