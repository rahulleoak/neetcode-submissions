class Solution:
    def wordFill(self, word):
        for idx in range(len(word)):
            pattern = word[:idx] + "*" + word[idx+1:]
            yield pattern
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 1
        
        words = set(wordList)
        if endWord not in words:
            return 0
        
        adjList = defaultdict(list)
        for word in wordList:
            for pattern in self.wordFill(word):
                adjList[pattern].append(word)
        

        q = deque([beginWord])
        visited = set([beginWord])
        hops = 0

        while q:
            hops += 1
            for _ in range(len(q)):
                currWord = q.popleft()

                if currWord == endWord:
                    return hops
                
                for pattern in self.wordFill(currWord):
                    for nei in adjList[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
                
        return 0
