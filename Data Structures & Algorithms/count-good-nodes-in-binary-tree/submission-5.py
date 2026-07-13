# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0 

        def dfs(node, localMax):
            nonlocal count
            
            if not node:
                return 0
            
            count += 1 if node.val >= localMax else 0
            localMax = max(localMax, node.val)

            dfs(node.left, localMax)
            dfs(node.right, localMax)
        
        dfs(root, root.val)
        return count