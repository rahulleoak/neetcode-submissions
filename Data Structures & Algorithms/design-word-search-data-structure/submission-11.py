class TrieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            
            curr = curr.children[ch]
        
        curr.endWord = True

    def dfs(self, idx, word, node):
        if idx == len(word):
            return node.endWord
        
        if word[idx] == ".":
            for ch in node.children.values():
                if self.dfs(idx+1, word, ch):
                    return True
            return False
        else:
            if word[idx] not in node.children:
                return False
            
            node = node.children[word[idx]]
            return self.dfs(idx+1, word, node)
        

    
    def search(self, word: str) -> bool:
        curr = self.root
        return self.dfs(0, word, curr)