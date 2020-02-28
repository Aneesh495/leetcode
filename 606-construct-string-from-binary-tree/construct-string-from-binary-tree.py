
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(node: Optional[TreeNode]) -> str:
            if not node:
                return ""
            res = str(node.val)
            if node.left or node.right:
                res += f"({dfs(node.left)})" if node.left else "()"
                if node.right:
                    res += f"({dfs(node.right)})"
            return res
        return dfs(root)
