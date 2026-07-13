"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        origToCopy = {} # original -> copy
        origToCopy[None] = None

        curr = head
        while curr:
            node = Node(curr.val)
            origToCopy[curr] = node
            curr = curr.next
        
        curr = head
        while curr:
            copy = origToCopy[curr]
            copy.next = origToCopy[curr.next]
            copy.random = origToCopy[curr.random]

            curr = curr.next
        
        return origToCopy[head]
