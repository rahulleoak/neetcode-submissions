# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        q = collections.deque()

        if root:
            q.append(root)
        else:
            return levels
        

        while q:
            levelLen = len(q)
            level = []
            for _ in range(levelLen):
                node = q.popleft()

                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            levels.append(level)
        
        return levels