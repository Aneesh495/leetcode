
from collections import deque

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, left=root)
        q = deque([root])
        current_depth = 1
        while q and current_depth < depth - 1:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            current_depth += 1
        for node in list(q):
            old_left = node.left
            old_right = node.right
            node.left = TreeNode(val, left=old_left)
            node.right = TreeNode(val, right=old_right)
        return root
