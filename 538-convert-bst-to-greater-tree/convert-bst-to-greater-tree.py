
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Maintain a running suffix sum of visited values
        total = 0

        def reverse_inorder(node: Optional[TreeNode]) -> None:
            nonlocal total
            if not node:
                return
            # Visit right subtree first because it has greater keys
            reverse_inorder(node.right)
            # Update running sum and replace node value
            total += node.val
            node.val = total
            # Then visit left subtree
            reverse_inorder(node.left)

        reverse_inorder(root)
        return root
