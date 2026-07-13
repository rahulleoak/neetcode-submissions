# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow
        prev = None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        start = head
        end = prev
        while end.next:
            start.next, start = end, start.next
            end.next, end= start, end.next
        
