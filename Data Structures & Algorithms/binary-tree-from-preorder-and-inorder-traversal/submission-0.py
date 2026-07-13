# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.preOrder = []
        self.inOrderMap = []
        self.rootKey = 0
    
    def dfsBuilder(self, left, right):
        if left > right:
            return
        
        rootVal = self.preOrder[self.rootKey]
        self.rootKey += 1
        root = TreeNode(rootVal)

        mid = self.inOrderMap[rootVal]
        root.left = self.dfsBuilder(left, mid - 1)
        root.right = self.dfsBuilder(mid + 1, right)

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preOrder = preorder
        self.inOrderMap = {val: idx for idx, val in enumerate(inorder)}

        return self.dfsBuilder(0, len(inorder) - 1)