
from typing import Optional, List
from collections import defaultdict

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        trees = {}
        count = defaultdict(int)
        res = []
        uid = 1

        def dfs(node):
            nonlocal uid
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            key = (node.val, l, r)
            if key not in trees:
                trees[key] = uid
                uid += 1
            tid = trees[key]
            count[tid] += 1
            if count[tid] == 2:
                res.append(node)
            return tid

        dfs(root)
        return res
