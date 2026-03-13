
from collections import deque
from typing import Optional

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([(root, 0)])
        ans = 0
        while q:
            first = q[0][1]
            last = first
            for _ in range(len(q)):
                node, idx = q.popleft()
                idx -= first
                last = idx
                if node.left:
                    q.append((node.left, 2 * idx + 1))
                if node.right:
                    q.append((node.right, 2 * idx + 2))
            ans = max(ans, last + 1)
        return ans
