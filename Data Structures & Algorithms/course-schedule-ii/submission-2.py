class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adjList = {i : [] for i in range(numCourses)}

        for dst, src in prerequisites:
            adjList[src].append(dst)
            indegree[dst] += 1
        
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)            

        res = []
        while q:
            curr = q.popleft()
            res.append(curr)

            for nei in adjList[curr]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)
        
        return res if len(res) == numCourses else []
        