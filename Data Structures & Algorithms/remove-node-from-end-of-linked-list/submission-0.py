# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        curr = head
        while curr:
            curr = curr.next
            N += 1
        

        removalIdx = N - n
        if removalIdx == 0:
            return head.next
        
        curr = head
        prev = None
        for i in range(removalIdx):
            curr, prev = curr.next, curr
        
        prev.next = curr.next

        return head

