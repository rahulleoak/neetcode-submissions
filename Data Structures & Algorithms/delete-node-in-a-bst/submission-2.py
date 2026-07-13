# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        keyParent = None
        curr = root
        while curr and curr.val != key:
            keyParent = curr

            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        
        # node not found
        if not curr:
            return root

        # CASE-1: no children or one child
        if not curr.left or not curr.right:
            # if target = root:
            child = curr.left if curr.left else curr.right
            if not keyParent:
                return child
            elif keyParent.left == curr:
                keyParent.left = child
            else:
                keyParent.right = child
        
        # CASE-2: has 2 children
        else:
            parent = delNode = curr
            
            # find inorder successor (leftmost node in right subtree)
            curr = curr.right
            while curr.left:
                parent = curr
                curr = curr.left
            
            if parent != delNode:
                parent.left = curr.right
                curr.right = delNode.right            
            curr.left = delNode.left

            # SubCASE: deleting root
            if not keyParent:
                return curr
            
            if keyParent.left == delNode:
                keyParent.left = curr
            else:
                keyParent.right = curr
        
        return root
