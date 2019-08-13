
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle empty list or single node
        if not head or not head.next:
            return head

        odd = head                 # Tail of odd index list
        even = head.next           # Tail of even index list
        even_head = even           # Head of even index list for final stitch

        # Rewire next pointers to build odd list followed by even list
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        # Append even list after odd list
        odd.next = even_head
        return head
