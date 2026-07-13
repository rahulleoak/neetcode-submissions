# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, pathMax):
            if not node:
                return 0
            
            goodNodeCount = 0
            if node.val >= pathMax:
                pathMax = node.val
                goodNodeCount += 1
            
            left = dfs(node.left, pathMax)
            right = dfs(node.right, pathMax)

            return goodNodeCount + left + right
        
        return dfs(root, root.val)