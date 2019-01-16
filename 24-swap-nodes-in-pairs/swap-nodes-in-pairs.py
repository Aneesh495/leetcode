
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node before head so edge cases are simple
        dummy = ListNode(0, head)
        prev = dummy  # Tail of the processed part that points to the next pair

        # While there are at least two nodes to swap
        while prev.next and prev.next.next:
            a = prev.next       # First node of the pair
            b = a.next          # Second node of the pair

            # Perform the swap of a and b
            a.next = b.next     # Link a to the node after b
            b.next = a          # Link b to a
            prev.next = b       # Link previous tail to b which is now first

            prev = a            # Move prev to a which is now the tail of the swapped pair

        return dummy.next       # New head after all swaps