# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodeCount = 0
        def dfs(node, lastMax):
            nonlocal goodNodeCount

            if not node:
                return [0, 0]
            
            count = 0
            if node.val >= lastMax:
                count += 1
                lastMax = node.val

            left, leftMax = dfs(node.left, lastMax)
            right, rightMax = dfs(node.right, lastMax)

            return left + right + count, lastMax
        
        return dfs(root, float('-inf'))[0]

