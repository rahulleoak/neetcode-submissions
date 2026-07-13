# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node: 
                return True,0
            
            leftB, leftH = dfs(node.left)
            rightB, rightH = dfs(node.right)

            
            balanced = leftB and rightB and abs(rightH - leftH) <= 1

            return balanced, 1 + max(leftH,rightH)
        
        b, h = dfs(root)
        return b