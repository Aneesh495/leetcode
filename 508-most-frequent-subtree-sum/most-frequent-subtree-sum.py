
# LeetCode 508. Most Frequent Subtree Sum
# Postorder DFS to compute each subtree sum once
# Time O(n)  Space O(n)

from collections import Counter
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findFrequentTreeSum(self, root: Optional['TreeNode']) -> List[int]:
        if not root:
            return []

        freq = Counter()

        def dfs(node: Optional['TreeNode']) -> int:
            # Return 0 for empty subtree
            if not node:
                return 0
            # Sum of current subtree = node value + left subtree sum + right subtree sum
            s = node.val + dfs(node.left) + dfs(node.right)
            freq[s] += 1
            return s

        dfs(root)
        max_freq = max(freq.values())
        return [s for s, c in freq.items() if c == max_freq]
