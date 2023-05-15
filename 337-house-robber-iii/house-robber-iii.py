
from typing import Optional, Tuple

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root: Optional['TreeNode']) -> int:
        """
        Returns the maximum money that can be robbed without robbing two directly-linked houses.
        Uses DFS with postorder traversal and returns a pair for each node:
          take  -> max if we rob this node
          skip  -> max if we don't rob this node
        """
        def dfs(node: Optional['TreeNode']) -> Tuple[int, int]:
            if not node:
                # take = 0 if we rob null
                # skip = 0 if we skip null
                return 0, 0

            left_take, left_skip = dfs(node.left)
            right_take, right_skip = dfs(node.right)

            # If we take current node we must skip both children
            take = node.val + left_skip + right_skip

            # If we skip current node we can choose best of take or skip for each child
            skip = max(left_take, left_skip) + max(right_take, right_skip)

            return take, skip

        take_root, skip_root = dfs(root)
        return max(take_root, skip_root)
