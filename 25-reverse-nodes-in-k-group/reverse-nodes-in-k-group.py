
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Count total nodes to know how many full groups exist
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        # Dummy node simplifies head handling
        dummy = ListNode(0, head)
        group_prev = dummy

        # Process while there are at least k nodes left
        while n >= k:
            # group_prev points to node before the group
            # group_end will become the last node of the reversed group
            group_end = group_prev.next
            cur = group_end.next

            # Reverse k-1 links inside the group using head insertion
            # After each step group_prev.next is the new head of the partially reversed group
            for _ in range(1, k):
                nxt = cur.next
                cur.next = group_prev.next
                group_prev.next = cur
                cur = nxt

            # Connect the tail of the reversed group to the remainder
            group_end.next = cur

            # Move group_prev to the end of the reversed group
            group_prev = group_end

            # Reduce remaining count
            n -= k

        return dummy.next