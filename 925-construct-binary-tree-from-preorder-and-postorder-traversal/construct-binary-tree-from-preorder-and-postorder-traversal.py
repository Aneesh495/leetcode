
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        i = j = 0
        def build():
            nonlocal i, j
            node = TreeNode(preorder[i])
            i += 1
            if node.val != postorder[j]:
                node.left = build()
            if node.val != postorder[j]:
                node.right = build()
            j += 1
            return node
        return build() if preorder else None
