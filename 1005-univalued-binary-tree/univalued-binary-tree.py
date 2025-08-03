
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        """
        Iterative DFS
        1. Record the value at the root
        2. Walk every node
        3. If any node value differs return False
        4. If all nodes match return True
        """
        if not root:
            return True

        target = root.val
        stack = [root]

        while stack:
            node = stack.pop()
            if not node:
                continue
            if node.val != target:
                return False
            # push children for DFS
            stack.append(node.left)
            stack.append(node.right)

        return True
