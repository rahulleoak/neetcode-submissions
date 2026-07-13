# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # Tree is basically rob/skip
        # Choice DP
        
        # skip = the best/max of each of the left and right children
        # take = "house" node value + all of the node's grandchilren values

        def dfs(node):
            if not node:
                # Base is just None node, robbing nothing gives nothing (0 = 0)
                return [0,0] # [skip, take]
            
            left = dfs(node.left)
            right = dfs(node.right)

            skip = max(left)  + max(right)
            take = node.val + left[0] + right[0]

            return [skip, take]

        
        return max(dfs(root))