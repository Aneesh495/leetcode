
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        """
        Postorder states per node:
          0 -> this node needs a camera
          1 -> this node has a camera
          2 -> this node is covered by a child camera
        Null returns 2 so leaves can decide correctly.
        """
        self.cameras = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 2  # Null is covered

            left = dfs(node.left)
            right = dfs(node.right)

            # If any child needs a camera place one here
            if left == 0 or right == 0:
                self.cameras += 1
                return 1  # This node now has a camera

            # If any child has a camera this node is covered
            if left == 1 or right == 1:
                return 2

            # Otherwise both children are covered but have no cameras
            # so this node needs a camera from its parent
            return 0

        # If root still needs a camera add one
        if dfs(root) == 0:
            self.cameras += 1

        return self.cameras
