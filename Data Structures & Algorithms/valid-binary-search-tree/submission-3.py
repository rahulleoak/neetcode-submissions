# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, currMin, currMax):
            if not node:
                return True
            
            if not (currMin < node.val < currMax):
                return False
            
            return validate(node.left, currMin, node.val) and validate(node.right, node.val, currMax)

        return validate(root, float('-inf'), float('inf'))