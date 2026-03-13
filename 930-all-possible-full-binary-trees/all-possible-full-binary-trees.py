
from functools import lru_cache

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        @lru_cache(None)
        def build(m: int):
            if m % 2 == 0:
                return tuple()
            if m == 1:
                return (TreeNode(0),)
            res = []
            for l in range(1, m, 2):
                r = m - 1 - l
                for left in build(l):
                    for right in build(r):
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        res.append(root)
            return tuple(res)
        return list(build(n))
