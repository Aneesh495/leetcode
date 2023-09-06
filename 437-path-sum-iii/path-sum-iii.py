
# LeetCode 437. Path Sum III
# Prefix sum with backtracking. O(n) time and O(h) extra space for recursion plus hashmap size up to n.

from typing import Optional
from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional['TreeNode'], targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1                           # empty path prefix

        ans = 0

        def dfs(node: Optional['TreeNode'], curr: int) -> None:
            nonlocal ans
            if not node:
                return

            curr += node.val                    # current prefix sum

            ans += prefix[curr - targetSum]     # paths ending here with target sum

            prefix[curr] += 1                   # add current prefix before exploring children
            dfs(node.left, curr)
            dfs(node.right, curr)
            prefix[curr] -= 1                   # remove when backtracking

        dfs(root, 0)
        return ans
