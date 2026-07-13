# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node, counter):
            if not node:
                return None, counter
            
            val, counter = dfs(node.left, counter)
            if val:
                return val, counter
            counter -= 1
            if counter == 0:
                return node.val, counter
            return dfs(node.right, counter)
        
        val,_ = dfs(root,k)
        return val