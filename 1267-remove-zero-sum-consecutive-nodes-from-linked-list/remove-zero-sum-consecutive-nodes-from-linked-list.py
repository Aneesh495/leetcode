class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        prefix = 0
        last_seen = {}
        curr = dummy

        while curr:
            prefix += curr.val
            last_seen[prefix] = curr
            curr = curr.next

        prefix = 0
        curr = dummy

        while curr:
            prefix += curr.val
            curr.next = last_seen[prefix].next
            curr = curr.next

        return dummy.next
