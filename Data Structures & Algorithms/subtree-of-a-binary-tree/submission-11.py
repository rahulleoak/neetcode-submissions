# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def serialize(self, node):
        serializedTree = []
        self.dfs(node, serializedTree)
        return ''.join(serializedTree)
    
    def dfs(self, node, res):
        if not node:
            res.append("#")
            return
        
        res.append(f"<{str(node.val)}>")
        self.dfs(node.left, res)
        self.dfs(node.right, res)
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        big = self.serialize(root)
        small = self.serialize(subRoot)

        return small in big