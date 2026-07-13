# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isBST(node, currMin, currMax):
            if not node:
                return True
            
            if not(currMin < node.val < currMax):
                return False
            
            return isBST(node.left, currMin, node.val) and isBST(node.right, node.val, currMax)
        
        return isBST(root, float('-inf'), float('inf'))
                