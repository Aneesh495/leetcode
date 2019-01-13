
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Use a dummy node before head to simplify deletion at head
        dummy = ListNode(0, head)
        first = dummy
        second = dummy

        # Move first ahead by n plus one to create a gap of n nodes
        for _ in range(n + 1):
            first = first.next

        # Move both pointers until first reaches the end
        while first:
            first = first.next
            second = second.next

        # second is just before the target node
        target = second.next
        second.next = target.next

        # Optional cleanup to avoid lingering references
        target.next = None

        return dummy.next