# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy.next
        curr = head

        while curr:
            prev, curr.next, curr  = curr, prev, curr.next 
        
        return prev