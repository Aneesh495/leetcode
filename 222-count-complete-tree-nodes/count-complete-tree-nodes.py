
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # For a complete binary tree the subtree is perfect if the leftmost depth equals the rightmost depth
        # A perfect subtree with depth d has 2^d minus 1 nodes
        # Otherwise count the root plus the counts of left and right subtrees. This runs in log squared time

        def left_depth(node: Optional[TreeNode]) -> int:
            d = 0
            while node:
                d += 1
                node = node.left
            return d

        def right_depth(node: Optional[TreeNode]) -> int:
            d = 0
            while node:
                d += 1
                node = node.right
            return d

        def solve(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            ld = left_depth(node)
            rd = right_depth(node)
            if ld == rd:
                return (1 << ld) - 1
            return 1 + solve(node.left) + solve(node.right)

        return solve(root)
