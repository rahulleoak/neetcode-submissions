import heapq as hq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)

        for src, dst, time in times:
            adjList[src].append((dst, time))
        
        shortestPath = {}
        shortestPath[k] = 0
        pq = [(0, k)]

        totalTime = 0
        while pq:
            timeSpent, node = hq.heappop(pq)

            if node in shortestPath and shortestPath[node] < timeSpent:
                continue
            
            totalTime = timeSpent

            for nei, neiW in adjList[node]:
                newTime = timeSpent + neiW

                if nei not in shortestPath or shortestPath[nei] > newTime:
                    shortestPath[nei] = newTime
                    hq.heappush(pq, (newTime, nei))
        
        return totalTime if len(shortestPath) == n else -1
