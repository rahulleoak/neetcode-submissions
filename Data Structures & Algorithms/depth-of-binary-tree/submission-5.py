# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxDepth = 0
        
        def dfs(node, currDepth):
            nonlocal maxDepth
            if not node:
                return 
            
            maxDepth = max(maxDepth, currDepth)

            dfs(node.left, currDepth + 1)
            dfs(node.right, currDepth + 1)
    
        dfs(root,1)
        return maxDepth


        

    '''
    BFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        if root:
            q.append(root)

        depth = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)            
            depth += 1

        return depth
    '''