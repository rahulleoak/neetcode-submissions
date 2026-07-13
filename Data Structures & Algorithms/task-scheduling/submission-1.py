class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqCount = Counter(tasks)
        taskCount = [cnt for cnt in freqCount.values()]
        taskCount.sort()
        
        chunks = taskCount.pop() - 1
        idleTime = chunks * n

        for task in taskCount:
            idleTime -= min(chunks, task)
        
        return len(tasks) + (idleTime if idleTime > 0 else 0)

