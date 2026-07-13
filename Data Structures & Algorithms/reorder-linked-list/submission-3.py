# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse from middle
        mid = slow
        prev = None
        while mid:
            mid.next, prev, mid = prev, mid, mid.next

        start = head
        end = prev
        while end.next:
            start.next, start = end, start.next
            end.next, end = start, end.next
        