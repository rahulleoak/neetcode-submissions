class ListNode:
    def __init__(self, key, val, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}

        self.first = ListNode(0, 0)
        self.last = ListNode(0, 0)

        self.first.next = self.last
        self.last.prev = self.first

    def insert(self, node):
        left, right = self.last.prev, self.last
        left.next = right.prev = node
        node.next = right
        node.prev = left

    def remove(self, node):
        left, right = node.prev, node.next
        left.next = right
        right.prev = left

    def get(self, key: int) -> int:
        if key in self.map:
            self.remove(self.map[key])
            self.insert(self.map[key])
            return self.map[key].val
        return -1     

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])
        
        self.map[key] = ListNode(key, value)
        self.insert(self.map[key])

        if len(self.map) > self.cap:
            lru = self.first.next
            self.remove(lru)
            del self.map[lru.key]
