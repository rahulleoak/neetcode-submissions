# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def sameTree(self, treeA, treeB):
        if not treeA and not treeB:
            return True
        if not treeA or not treeB or treeA.val != treeB.val:
            return False
        
        return self.sameTree(treeA.left, treeB.left) and self.sameTree(treeA.right, treeB.right)


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return False
        
        if root.val == subRoot.val:
            if self.sameTree(root, subRoot):
                return True
        
        return self.isSubtree(root.left, subRoot)  or self.isSubtree(root.right, subRoot)