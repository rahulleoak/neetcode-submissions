# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderDFS(self, root):
        if not root: 
            return 0

        left = self.postorderDFS(root.left)
        if left == -1:
            return -1

        right = self.postorderDFS(root.right)
        if right == -1:
            return -1

        if abs(right - left) > 1:
            return -1
        
        return max(left, right) + 1
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanceCheck = self.postorderDFS(root)
        return balanceCheck != -1