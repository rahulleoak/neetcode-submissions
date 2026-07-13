# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def dfs(node, parent):
            if not node:
                return 0
            
            goodNode = 0
            if node.val >= parent:
                goodNode += 1
                parent = node.val

            left = dfs(node.left, parent)
            right = dfs(node.right, parent)

            return goodNode + left + right

        return dfs(root, float('-inf'))