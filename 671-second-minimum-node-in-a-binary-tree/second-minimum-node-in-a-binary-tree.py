
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        first = root.val
        ans = float('inf')

        def dfs(node):
            nonlocal ans
            if not node:
                return
            if first < node.val < ans:
                ans = node.val
                return
            if node.val == first:
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return -1 if ans == float('inf') else ans
