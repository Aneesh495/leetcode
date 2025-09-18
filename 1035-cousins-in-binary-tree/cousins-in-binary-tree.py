
from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCousins(self, root: Optional['TreeNode'], x: int, y: int) -> bool:
        """
        Level order traversal.
        Track parent for each node at the current level.
        x and y are cousins if they appear in the same level and have different parents.
        """
        if not root:
            return False

        q = deque([(root, None)])  # pair of node and its parent

        while q:
            level_size = len(q)
            x_parent = None
            y_parent = None

            for _ in range(level_size):
                node, parent = q.popleft()

                if node.val == x:
                    x_parent = parent
                if node.val == y:
                    y_parent = parent

                if node.left:
                    q.append((node.left, node))
                if node.right:
                    q.append((node.right, node))

            # After processing one level check if x and y were found here
            if x_parent or y_parent:
                return x_parent is not None and y_parent is not None and x_parent != y_parent

        return False
