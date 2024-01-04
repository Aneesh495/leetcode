
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        Inorder traversal yields sorted values for a BST.
        Track the previous value seen and update the best gap at each step.
        Time O(n). Space O(h) for recursion where h is tree height.
        """
        prev = None
        best = float("inf")

        def inorder(node: Optional[TreeNode]) -> None:
            nonlocal prev, best
            if not node:
                return
            inorder(node.left)
            if prev is not None:
                best = min(best, node.val - prev)
            prev = node.val
            inorder(node.right)

        inorder(root)
        return best
