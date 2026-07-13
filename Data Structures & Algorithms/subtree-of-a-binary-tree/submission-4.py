# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def serialize(self, root):
        s = []
        def dfs(node):
            nonlocal s
            if not node:
                s.append("#")
                return
            s.append(",")
            s.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ''.join(s)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        big = self.serialize(root)
        small = self.serialize(subRoot)

        return small in big














