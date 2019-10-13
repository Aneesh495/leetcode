
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # dfs returns the sum of left leaf values under node
        # is_left flags whether current node is a left child of its parent
        def dfs(node: Optional[TreeNode], is_left: bool) -> int:
            if not node:
                return 0
            # if leaf then count it only when it is a left child
            if not node.left and not node.right:
                return node.val if is_left else 0
            # explore left as left child and right as not left
            return dfs(node.left, True) + dfs(node.right, False)

        return dfs(root, False)