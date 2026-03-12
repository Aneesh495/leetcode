
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional

class Solution:
    def findMode(self, root: Optional['TreeNode']) -> List[int]:
        # In a BST the inorder traversal visits values in sorted order
        # We can count consecutive equal values in a single pass
        # To avoid extra space we do two inorder passes
        # Pass one finds the maximum frequency and how many values reach it
        # Pass two collects the values that reach the maximum frequency

        if not root:
            return []

        self.cur_val = None       # current value being counted
        self.cur_count = 0        # count of the current value
        self.max_count = 0        # best frequency seen so far
        self.mode_count = 0       # number of values that tie for best frequency
        self.modes = []           # filled in the second pass

        def handle_value(val: int, collecting: bool) -> None:
            # Update the run length for the incoming value
            if self.cur_val != val:
                self.cur_val = val
                self.cur_count = 0
            self.cur_count += 1

            # Improve maximum or record a tie
            if self.cur_count > self.max_count:
                self.max_count = self.cur_count
                self.mode_count = 1
                if collecting:
                    self.modes[0] = val
            elif self.cur_count == self.max_count:
                if collecting:
                    self.modes[self.mode_count] = val
                self.mode_count += 1

        def inorder(node: Optional['TreeNode'], collecting: bool) -> None:
            if not node:
                return
            inorder(node.left, collecting)
            handle_value(node.val, collecting)
            inorder(node.right, collecting)

        # First pass to compute max_count and mode_count
        inorder(root, collecting=False)

        # Prepare storage for modes based on mode_count from pass one
        self.modes = [0] * self.mode_count

        # Reset trackers for the second pass
        self.cur_val = None
        self.cur_count = 0
        self.mode_count = 0

        # Second pass to collect the actual modes
        inorder(root, collecting=True)

        return self.modes
