'''
def sameTree(self, treeA, treeB):
    if not treeA and not treeB:
        return True
    if not treeA or not treeB or treeA.val != treeB.val:
        return False
    
    return self.sameTree(treeA.left, treeB.left) and self.sameTree(treeA.right, treeB.right)


def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if not subRoot:
        return True
    
    if not root: # indicative of the fact that if we hit the leaf node, we were not able to find a match
        return False
    
    if root.val == subRoot.val:
        if self.sameTree(root, subRoot):
            return True
    
    return self.isSubtree(root.left, subRoot)  or self.isSubtree(root.right, subRoot)
'''
class Solution: 
    def flatten(self, node):
        flattened = []

        def dfs(node):    
            if not node:
                flattened.append("#")
                return

            dfs(node.left)
            dfs(node.right)  
            flattened.append(f"<{node.val}>")
        
        dfs(node)
        return ''.join(flattened)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        big = self.flatten(root)
        small = self.flatten(subRoot)

        return small in big