
from typing import Optional

# LeetCode provides TreeNode
class Solution:
    def distributeCoins(self, root: Optional['TreeNode']) -> int:
        # Postorder return net balance of coins for this subtree
        # Balance equals coins in subtree minus nodes in subtree
        # Moves add absolute balances from children since each unit must travel across the edge once
        moves = 0

        def dfs(node: Optional['TreeNode']) -> int:
            nonlocal moves
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            moves += abs(left) + abs(right)
            return node.val + left + right - 1

        dfs(root)
        return moves
