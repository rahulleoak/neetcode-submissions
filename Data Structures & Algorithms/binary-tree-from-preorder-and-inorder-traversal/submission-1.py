# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderMap = {val:idx for idx, val in enumerate(inorder)}
        n = len(inorder) - 1
        rootIdx = [0]
        
        def dfs(inLower, inUpper): 
            if inLower > inUpper:
                return None
            
            rootVal = preorder[rootIdx[0]]
            rootIdx[0] += 1
            node = TreeNode(rootVal)
            inorderRootIdx = inorderMap[rootVal]
                    
            node.left = dfs(inLower, inorderRootIdx - 1)
            node.right = dfs(inorderRootIdx + 1, inUpper)

            return node
        
        root = dfs(0,n)
        return root