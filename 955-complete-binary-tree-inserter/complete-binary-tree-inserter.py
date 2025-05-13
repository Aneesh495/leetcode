
from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CBTInserter:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.q = deque()
        dq = deque([root])
        while dq:
            node = dq.popleft()
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
            if not node.left or not node.right:
                self.q.append(node)

    def insert(self, val: int) -> int:
        parent = self.q[0]
        node = TreeNode(val)
        if not parent.left:
            parent.left = node
        else:
            parent.right = node
            self.q.popleft()
        self.q.append(node)
        return parent.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root
