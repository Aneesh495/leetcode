
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Iterates down the tree to find the node and rebuilds links on the way back

        def min_node(node: TreeNode) -> TreeNode:
            # Returns the leftmost node in this subtree
            while node.left:
                node = node.left
            return node

        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root

        # Found the node to delete
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        # Node has two children
        succ = min_node(root.right)        # inorder successor
        root.val = succ.val                # copy value
        root.right = self.deleteNode(root.right, succ.val)  # delete successor
        return root
