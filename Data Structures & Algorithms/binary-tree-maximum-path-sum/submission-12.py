# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')

        def dfs(node):
            nonlocal maxSum

            if not node:
                return 0
            
            leftPathSum = dfs(node.left)
            leftPathSum = max(leftPathSum, 0)

            rightPathSum = dfs(node.right)
            rightPathSum = max(rightPathSum, 0)
        
            maxSum = max(maxSum, node.val + leftPathSum + rightPathSum)

            return node.val + max(leftPathSum,rightPathSum)

        dfs(root)
        return maxSum