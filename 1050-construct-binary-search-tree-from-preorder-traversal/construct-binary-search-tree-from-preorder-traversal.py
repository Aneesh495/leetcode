
# LeetCode 1008. Construct BST from Preorder
# Use a shared index that walks preorder once
# Each call respects current bounds and returns a subtree

from math import inf
from typing import List, Optional

# LeetCode supplies TreeNode
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        i = 0  # shared cursor in preorder
        
        def build(lower: int, upper: int) -> Optional[TreeNode]:
            nonlocal i
            # stop if we used all values
            if i == len(preorder):
                return None
            val = preorder[i]
            # value must lie within current bounds
            if not (lower < val < upper):
                return None
            # consume the value
            i += 1
            node = TreeNode(val)
            # build left with updated upper bound
            node.left = build(lower, val)
            # build right with updated lower bound
            node.right = build(val, upper)
            return node
        
        # start with infinite bounds
        return build(-inf, inf)
