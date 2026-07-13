# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        nodes = []
        def dfs(node, pathMax):
            if not node:
                return 0
            
            goodNodeCount = 0
            if node.val >= pathMax:
                goodNodeCount += 1
                nodes.append(node.val)
                pathMax = node.val

            leftCount = dfs(node.left, pathMax)
            rightCount = dfs(node.right, pathMax)

            return leftCount + rightCount + goodNodeCount
        
        count =  dfs(root, root.val)
        print(nodes)
        return len(nodes)
        
