# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node):
            nonlocal k
            if not node:
                return None
            
            res = dfs(node.left)
            if res is not None: 
                return res
            
            k -= 1
            if k == 0: 
                return node.val

            return dfs(node.right)
        
        return dfs(root)