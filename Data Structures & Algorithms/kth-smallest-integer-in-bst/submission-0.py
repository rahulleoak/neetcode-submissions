# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node, path):
            if not node:
                return
            
            dfs(node.left, path)
            path.append(node.val)
            dfs(node.right, path)

            return path
        
        path = dfs(root,[])

        if k > len(path):
            return -1
        return path[k-1]