
from collections import deque
from typing import List, Optional

# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            level_size = len(q)
            level = []
            for _ in range(level_size):
                node = q.popleft()
                level.append(node.val)
                for child in node.children:
                    if child:
                        q.append(child)
            res.append(level)
        return res
