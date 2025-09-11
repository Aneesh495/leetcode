
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional['TreeNode']) -> str:
        # Depth first search collects path from root to current node as letters
        # At a leaf build string from leaf to root and update answer if smaller
        best = None
        path = []

        def dfs(node: Optional['TreeNode']) -> None:
            nonlocal best
            if not node:
                return

            # Map value 0..25 to letter a..z
            path.append(chr(ord('a') + node.val))

            if not node.left and not node.right:
                cand = ''.join(reversed(path))
                if best is None or cand < best:
                    best = cand
            else:
                dfs(node.left)
                dfs(node.right)

            # Backtrack
            path.pop()

        dfs(root)
        return best or ""
