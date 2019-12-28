
from typing import Optional
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional['TreeNode']) -> int:
        # BFS level-order. The first node of each level is the leftmost.
        q = deque([root])
        leftmost = root.val

        while q:
            level_size = len(q)
            leftmost = q[0].val  # first node at this level
            for _ in range(level_size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return leftmost
