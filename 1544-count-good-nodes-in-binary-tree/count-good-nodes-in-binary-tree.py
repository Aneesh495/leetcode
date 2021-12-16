class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        stack = [(root, float("-inf"))]
        while stack:
            node, maximum = stack.pop()
            result += node.val >= maximum
            maximum = max(maximum, node.val)
            if node.left: stack.append((node.left, maximum))
            if node.right: stack.append((node.right, maximum))
        return result