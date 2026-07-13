class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i : [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for dst, src in prerequisites:
            adjList[src].append(dst)
            indegree[dst] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        visited = 0
        while q:
            curr = q.popleft()
            
            visited += 1

            for nei in adjList[curr]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)
        
        return visited == numCourses
            