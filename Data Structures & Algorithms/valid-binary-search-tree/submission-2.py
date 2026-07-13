# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, currMin, currMax):
            if not node:
                return True
            
            if not (currMin < node.val < currMax):
                return False
            
            return dfs(node.left, currMin, node.val) and dfs(node.right, node.val, currMax)
    
        return dfs(root, float("-inf"), float("inf"))
                
