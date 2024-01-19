
# LeetCode 543 Diameter of Binary Tree
# Depth first search returns height for each node
# Track the best diameter seen so far as the sum of left and right heights

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0  # global diameter in edges

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0  # empty subtree height is zero
            lh = dfs(node.left)   # height from left child
            rh = dfs(node.right)  # height from right child
            # path through this node uses lh edges down left plus rh edges down right
            if lh + rh > self.best:
                self.best = lh + rh
            return 1 + lh if lh >= rh else 1 + rh  # height of this subtree

        dfs(root)
        return self.best
