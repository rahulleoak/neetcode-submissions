# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:       
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def match(main, sub):
            if not main and not sub:
                return True
            
            if not main or not sub or main.val != sub.val:
                return False
            
            return match(main.left, sub.left) and match(main.right, sub.right) 
        
        if not subRoot:
            return True
        if not root:
            return False
        
        if root.val == subRoot.val and match(root, subRoot):
                return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)