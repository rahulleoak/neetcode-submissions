# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        levelOrder = []
        q = deque([root])

        while q:
            level = []
            for _ in range(len(q)):
                currNode = q.popleft()
                level.append(currNode.val)

                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)
            
            levelOrder.append(level)
        
        return levelOrder