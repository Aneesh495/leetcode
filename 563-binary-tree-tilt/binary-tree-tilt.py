
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        total_tilt = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal total_tilt
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            total_tilt += abs(l - r)
            return l + r + node.val

        dfs(root)
        return total_tilt
