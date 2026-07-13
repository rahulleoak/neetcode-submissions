# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node,currMax):
            if not node:
                return 0

            visible = 0
            if node.val >= currMax:
                visible += 1
                currMax = node.val
            
            left = dfs(node.left, currMax)
            right = dfs(node.right, currMax)

            return visible + left + right

        return dfs(root, root.val)