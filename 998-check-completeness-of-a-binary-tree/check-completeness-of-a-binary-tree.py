
from typing import Optional
from collections import deque

# LeetCode provides the TreeNode class
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCompleteTree(self, root: Optional['TreeNode']) -> bool:
        """
        Level order traversal
        Once a null is seen every later node must also be null
        If a non null node appears after a null the tree is not complete
        """
        q = deque([root])
        seen_null = False

        while q:
            node = q.popleft()

            if node is None:
                seen_null = True
                continue

            if seen_null:
                return False

            q.append(node.left)
            q.append(node.right)

        return True
