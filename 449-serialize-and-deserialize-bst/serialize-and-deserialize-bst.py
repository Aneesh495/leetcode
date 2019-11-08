
class Codec:
    def serialize(self, root):
        vals = []
        def preorder(node):
            if not node:
                return
            vals.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return " ".join(vals)

    def deserialize(self, data):
        if not data:
            return None
        vals = list(map(int, data.split()))
        i = 0
        def build(lo, hi):
            nonlocal i
            if i == len(vals):
                return None
            v = vals[i]
            if not (lo < v < hi):
                return None
            i += 1
            node = TreeNode(v)
            node.left = build(lo, v)
            node.right = build(v, hi)
            return node
        return build(float("-inf"), float("inf"))
