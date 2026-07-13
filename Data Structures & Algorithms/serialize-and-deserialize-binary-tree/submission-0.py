# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        output = []

        def dfs(node):
            if not node:
                output.append("#")
                return
            
            output.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        return ",".join(output)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        decoded = data.split(",")
        idx = 0
        
        def dfs():
            nonlocal idx
            val = decoded[idx]

            if val == "#":
                idx += 1
                return None
            

            node = TreeNode(int(val))
            idx += 1

            node.left = dfs()
            node.right = dfs()

            return node
        
        
        return dfs()
        
            
        