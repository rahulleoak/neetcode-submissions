class ListNode:
    def __init__(self, key = 0, val = 0, prev = None, next = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.size = capacity
        
        self.start = ListNode()
        self.end = ListNode()
        
        self.start.next = self.end
        self.end.prev = self.start

    def insert(self, node):
        lastNode = self.end.prev
        lastPtr = self.end

        node.prev = lastNode
        node.next = lastPtr

        self.end.prev = node
        lastNode.next = node
    
    def delete(self, node):
        nodeNext = node.next
        nodePrev = node.prev

        nodePrev.next = nodeNext
        nodeNext.prev = nodePrev


    def get(self, key: int) -> int:
        if key in self.cache:
            self.delete(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
        
        self.cache[key] = ListNode(key,value)
        self.insert(self.cache[key])

        if self.size < len(self.cache):
            lruNode = self.start.next
            lruKey = lruNode.key
            self.delete(lruNode)
            del self.cache[lruKey]


