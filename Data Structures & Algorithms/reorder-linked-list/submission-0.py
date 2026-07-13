# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        fast = head
        while fast and fast.next:
            curr = curr.next
            fast = fast.next.next
        
        dummy = ListNode()
        prev = dummy.next
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        first = head
        second = prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
        
        