# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        node = TreeNode(val)

        if not root:
            root = node
            return root

        while True:
            if val > curr.val:
                if not curr.right:
                    curr.right = node
                    return root
                curr = curr.right
            elif val < curr.val:
                if not curr.left:
                    curr.left = node
                    return root
                curr = curr.left
            