
# Definition for a Node.
class Node:
    def __init__(self, val: int = None, children: list["Node"] | None = None):
        self.val = val
        self.children = children or []

class Solution:
    def postorder(self, root: "Node") -> list[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.children:
                stack.extend(node.children)
        return res[::-1]
