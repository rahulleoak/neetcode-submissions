class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adjList = {i : [] for i in range(numCourses)}

        for dst, src in prerequisites:
            adjList[src].append(dst)
            indegree[dst] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        visited = set()
        while q:
            node = q.popleft()

            visited.add(node)

            for nei in adjList[node]:
                if nei not in visited:
                    indegree[nei] -= 1

                    if indegree[nei] == 0:
                        q.append(nei)
        
        return len(visited) == numCourses
        