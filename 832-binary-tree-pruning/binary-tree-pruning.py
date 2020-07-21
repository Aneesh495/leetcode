
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def prune(node):
            if not node:
                return None
            node.left = prune(node.left)
            node.right = prune(node.right)
            if node.val == 0 and node.left is None and node.right is None:
                return None
            return node
        return prune(root)
