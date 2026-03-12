
from collections import deque
from typing import Optional

# BFS to find the first leaf
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([(root, 1)])  # node with depth

        while q:
            node, depth = q.popleft()

            # leaf reached so this is the minimum depth
            if not node.left and not node.right:
                return depth

            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))
