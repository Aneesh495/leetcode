
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from typing import List, Optional

class Solution:
    def verticalTraversal(self, root: Optional['TreeNode']) -> List[List[int]]:
        # BFS to record each node as (col, row, val)
        if not root:
            return []
        nodes = []
        q = deque([(root, 0, 0)])  # node, row, col
        while q:
            node, r, c = q.popleft()
            nodes.append((c, r, node.val))
            if node.left:
                q.append((node.left, r + 1, c - 1))
            if node.right:
                q.append((node.right, r + 1, c + 1))

        # Sort by column then row then value
        nodes.sort()  # Python tuple sort: (col, row, val)

        # Group by column
        res = []
        prev_col = None
        for c, r, v in nodes:
            if c != prev_col:
                res.append([])
                prev_col = c
            res[-1].append(v)
        return res
