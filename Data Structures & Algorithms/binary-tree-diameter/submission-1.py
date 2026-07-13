# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0
    
    def postOrderLRC(self, root):
        if not root:
            return 0
        
        leftHeight = self.postOrderLRC(root.left)
        rightHeight = self.postOrderLRC(root.right)

        self.diameter = max(self.diameter, leftHeight+rightHeight)

        return max(leftHeight,rightHeight) + 1
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.postOrderLRC(root)
        return self.diameter