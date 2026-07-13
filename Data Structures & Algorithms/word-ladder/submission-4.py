class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 1
        
        words = set(wordList)
        if endWord not in words:
            return 0
        
        def generatePatterns(word):
            for i in range(len(word)):
                yield word[:i] + "*" + word[i+1:]
        
        adjList = defaultdict(list)
        for word in wordList:
            for pattern in generatePatterns(word):
                adjList[pattern].append(word)
        
        q = deque([beginWord])
        visited = set([beginWord])
        seqCount = 1

        while q:
            for _ in range(len(q)):
                currWord = q.popleft()

                if currWord == endWord:
                    return seqCount
                
                for pattern in generatePatterns(currWord):
                    for nei in adjList[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            seqCount += 1
        
        return 0


        
