class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]

        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.root
        stack = [(curr,0)]

        while stack:
            node, idx = stack.pop()
            
            if idx == len(word):
                if node.word:
                    return True
                continue
            
            c = word[idx]

            if c == ".":
                for ch in node.children:
                    stack.append((node.children[ch], idx + 1))
            else:
                if c in node.children:
                    stack.append((node.children[c], idx + 1))

        
        return False





