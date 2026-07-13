class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        indegree = [0] * numCourses

        for dst, src in prerequisites:
            adjList[src].append(dst)
            indegree[dst] += 1
        

        q = deque([node for node in range(numCourses) if indegree[node] == 0])
        visited = set([node for node in range(numCourses) if indegree[node] == 0])

        while q:
            curr = q.popleft()

            for nei in adjList[curr]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    visited.add(nei)
                    q.append(nei)
        
        return len(visited) == numCourses