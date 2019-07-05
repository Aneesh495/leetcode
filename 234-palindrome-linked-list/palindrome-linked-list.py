
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Reverse a linked list and return new head
        def reverse(node: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            curr = node
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        if not head or not head.next:
            return True

        # Find middle using slow and fast pointers
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # If odd length skip the middle node
        if fast:
            second = reverse(slow.next)
        else:
            second = reverse(slow)

        first = head
        ok = True
        cur2 = second
        while cur2:
            if first.val != cur2.val:
                ok = False
                break
            first = first.next
            cur2 = cur2.next

        return ok
