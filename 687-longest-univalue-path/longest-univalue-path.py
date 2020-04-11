
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.best = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)

            left_path = l + 1 if node.left and node.left.val == node.val else 0
            right_path = r + 1 if node.right and node.right.val == node.val else 0

            self.best = max(self.best, left_path + right_path)
            return max(left_path, right_path)

        dfs(root)
        return self.best
