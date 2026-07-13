# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "#"

        q = collections.deque([root])
        encoded = []

        while q:
            currNode = q.popleft()
        
            if currNode:
                encoded.append(str(currNode.val))
                q.append(currNode.left)
                q.append(currNode.right)
            else:
                encoded.append("#")
        
        return ','.join(encoded)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "#":
            return None
        
        data = data.split(",")
        root = TreeNode(int(data[0]))
        currIdx = 1

        q = deque([root])
        while q:
            currNode = q.popleft()

            leftNode = self.buildNode(data[currIdx])
            if leftNode:    
                currNode.left = leftNode
                q.append(leftNode)
            currIdx += 1
            
            rightNode = self.buildNode(data[currIdx])
            if rightNode:    
                currNode.right = rightNode
                q.append(rightNode)
            currIdx += 1
    
        return root

    def buildNode(self, value):
        if value != "#":
            return TreeNode(int(value))
        return None
