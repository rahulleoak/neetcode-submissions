import heapq as hq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = { i+1 : [] for i in range(n)}

        for src, dst, time in times:
            adjList[src].append((time,dst))
        
        visited = set()
        # pq = prio queue
        pq = [(0,k)]
        
        timeTaken = 0
        while pq:
            currT, currNode = hq.heappop(pq)
            
            if currNode in visited:
                continue
            
            visited.add(currNode)
            timeTaken = currT

            if len(visited) == n:
                return timeTaken

            for neiTime, nei in adjList[currNode]:
                if nei not in visited:
                    hq.heappush(pq,(currT + neiTime, nei))

        return -1
            

