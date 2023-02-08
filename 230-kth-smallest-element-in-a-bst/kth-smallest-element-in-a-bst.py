
# Definition for a binary tree node is provided by the platform
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Inorder traversal of a BST visits nodes in ascending order
        # Use an explicit stack to achieve O(h) space and O(k) time until answer
        stack = []
        node = root

        while True:
            # Go left as far as possible and push the path to the stack
            while node:
                stack.append(node)
                node = node.left

            # Visit next node in sorted order
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val

            # Move to the right subtree to continue inorder traversal
            node = node.right
