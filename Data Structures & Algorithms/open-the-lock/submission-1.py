class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visit = set(deadends)
        if "0000" in visit or target in visit:
            return -1
        if "0000" == target:
            return 0
        
        def neighbours(combo):
            for i in range(4):
                val = int(combo[i])

                for shift in [-1,1]:
                    change = (val + shift) % 10
                    yield combo[:i] + str(change) + combo[i+1:]
        
        q = deque([("0000", 0)])
        visit.add('0000')

        while q:
            lock, turns = q.popleft()
            if lock == target:
                return turns
            for child in neighbours(lock):
                if child not in visit:
                    visit.add(child)
                    q.append((child, turns + 1))
        return -1