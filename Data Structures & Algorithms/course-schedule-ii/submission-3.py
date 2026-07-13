class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {i : [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for dst, src in prerequisites:
            adjList[src].append(dst)
            indegree[dst] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        

        res = []
        while q:
            node = q.popleft()

            res.append(node)

            for nei in adjList[node]:
                indegree[nei] -= 1
                
                if indegree[nei] == 0:
                    q.append(nei)
        
        return res if len(res) == numCourses else []
