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
        if not head:
            return None
        
        curr = head
        while curr:
            nxt = curr.next
            copy = Node(curr.val)

            curr.next = copy
            copy.next = nxt

            curr = nxt
        
        curr = head
        while curr:
            if curr.random:
               curr.next.random = curr.random.next
            curr = curr.next.next
        
        curr = head
        copyHead = head.next if head.next else None
        while curr:
            copy = curr.next
            nxtCurr = copy.next      

            curr.next = nxtCurr
            copy.next = nxtCurr.next if nxtCurr else None

            curr = curr.next

        return copyHead