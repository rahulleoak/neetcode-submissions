# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return (0,0) #Height, Diameter
                      
            leftH, leftD = dfs(node.left)
            rightH, rightD = dfs(node.right)

            currH = 1 + max(leftH, rightH)
            currD = max(leftD, rightD, leftH + rightH)
            
            return currH, currD
        
        height, diameter = dfs(root)
        return diameter