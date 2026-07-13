# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return 
        
        if key == root.val:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right  
            elif not root.left and not root.right:
                return None
            else:
                curr = root.right
                while curr.left:
                    curr = curr.left
                root.val = curr.val
                root.right = self.deleteNode(root.right, curr.val)


        if key < root.val:
            root.left  = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        return root
