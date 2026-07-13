# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        encoded = []

        def breakTree(node):
            if not node:
                encoded.append("#")
                return 
            
            encoded.append(str(node.val))
            breakTree(node.left)
            breakTree(node.right)

        
        breakTree(root)
        return ",".join(encoded)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(",")
        currIdx = 0

        def makeTree():
            nonlocal currIdx
            
            if data[currIdx] == "#":
                currIdx += 1
                return None
            
            node = TreeNode(int(data[currIdx]))
            currIdx += 1
            node.left = makeTree()
            node.right = makeTree()

            return node

        return makeTree()
            