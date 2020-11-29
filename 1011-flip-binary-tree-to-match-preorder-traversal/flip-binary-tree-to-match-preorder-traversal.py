
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional

class Solution:
    def flipMatchVoyage(self, root: Optional['TreeNode'], voyage: List[int]) -> List[int]:
        """
        Return a list of node values where flips happen to match the given preorder voyage.
        If impossible return [-1].
        Preorder is root then left then right.
        A flip swaps a node's left and right children.
        Strategy
          Walk the tree in preorder while advancing a pointer over voyage
          When the next expected value does not match the left child we flip at this node
          Then we traverse right first then left which simulates the swap
        Time O(n)
        Space O(h) recursion stack where h is tree height
        """
        self.i = 0
        self.v = voyage
        self.flips = []
        self.ok = True

        def dfs(node: Optional['TreeNode']) -> None:
            if not node or not self.ok:
                return
            # The current node must match the current voyage value
            if self.i >= len(self.v) or node.val != self.v[self.i]:
                self.ok = False
                return
            self.i += 1

            # Decide whether we need a flip
            # If left exists and its value is not the next voyage value
            # then the next node in preorder must be the right child so we flip
            if node.left and self.i < len(self.v) and node.left.val != self.v[self.i]:
                self.flips.append(node.val)
                dfs(node.right)
                dfs(node.left)
            else:
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return self.flips if self.ok else [-1]
