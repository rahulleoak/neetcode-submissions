class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord:
            return 0
        
        
        wordChoice = set(wordList)
        if endWord not in wordChoice:
            return 0

        def generatePattern(word):
            for i in range(len(word)):
                yield word[:i] + "*" + word[i+1:]
        
        adjList = collections.defaultdict(list)
        for word in wordChoice:
            for pattern in generatePattern(word):
                adjList[pattern].append(word)
        
        start = {beginWord}
        end = {endWord}
        
        steps = 1
        while start and end:
            if len(start) > len(end):
                start, end = end, start
            
            nextLayer = set()
            for word in start:
                for pattern in generatePattern(word):
                    for possible in adjList[pattern]:
                        if possible in end:
                            return steps + 1
                        if possible in wordChoice:
                            nextLayer.add(possible)
                            wordChoice.remove(possible)
            
            steps += 1
            start = nextLayer
        
        return 0