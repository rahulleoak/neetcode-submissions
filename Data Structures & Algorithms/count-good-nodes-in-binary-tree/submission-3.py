# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, currMax):
            if not node:
                return 0
            
            goodNode = False
            if node.val >= currMax:
                goodNode = True
                currMax = node.val
            
            return goodNode + dfs(node.left, currMax) + dfs(node.right, currMax)
        
        return dfs(root, float("-inf"))
            