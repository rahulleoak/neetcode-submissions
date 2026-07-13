# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
    
        viewFromRight = []
        q = deque([root])

        while q:
            viewFromRight.append(q[0].val)
            for _ in range(len(q)):
                curr = q.popleft()
                
                if curr.right:
                    q.append(curr.right)
                if curr.left:
                    q.append(curr.left)
        
        return viewFromRight