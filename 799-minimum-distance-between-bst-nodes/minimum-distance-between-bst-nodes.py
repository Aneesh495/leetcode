
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev = None
        best = float('inf')

        def inorder(node):
            nonlocal prev, best
            if not node:
                return
            inorder(node.left)
            if prev is not None:
                best = min(best, node.val - prev)
            prev = node.val
            inorder(node.right)

        inorder(root)
        return int(best)
