# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = float('-inf')
        
        def dfs(node):
            nonlocal maxDiameter

            if not node:
                return 0
            
            leftDia = dfs(node.left)
            rightDia = dfs(node.right)

            currDiameter = max(leftDia, rightDia)
            maxDiameter = max(maxDiameter, leftDia + rightDia)

            return 1 + currDiameter
        
        dfs(root)
        return maxDiameter
