
from typing import List, Optional

# LeetCode provides TreeNode

class Solution:
    def printTree(self, root: Optional['TreeNode']) -> List[List[str]]:
        def height(node: Optional['TreeNode']) -> int:
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))

        h = height(root)
        w = (1 << h) - 1
        res = [["" for _ in range(w)] for _ in range(h)]

        def dfs(node: 'TreeNode', r: int, c: int):
            res[r][c] = str(node.val)
            if node.left:
                dfs(node.left, r + 1, c - (1 << (h - r - 2)))
            if node.right:
                dfs(node.right, r + 1, c + (1 << (h - r - 2)))

        dfs(root, 0, (w - 1) // 2)
        return res
