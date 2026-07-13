# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNodeWrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []

        for lst in lists:
            heapq.heappush(minHeap, ListNodeWrapper(lst))
        
        dummy = ListNode()
        curr = dummy

        while minHeap:
            nodeList = heapq.heappop(minHeap)
            node = nodeList.node

            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(minHeap, ListNodeWrapper(node.next))
        
        return dummy.next
