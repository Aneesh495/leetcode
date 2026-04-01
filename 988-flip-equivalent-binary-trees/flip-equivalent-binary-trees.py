
# Definition for a binary tree node is provided by the platform.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def flipEquiv(self, root1: Optional['TreeNode'], root2: Optional['TreeNode']) -> bool:
        # If both nodes are the same object then they are equivalent
        if root1 is root2:
            return True
        # If either node is missing or values differ then not equivalent
        if not root1 or not root2 or root1.val != root2.val:
            return False
        # Check without a flip
        same = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        # Check with a flip
        flipped = self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
        # Trees are flip equivalent if either condition holds
        return same or flipped
