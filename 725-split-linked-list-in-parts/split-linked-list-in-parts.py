class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n, node = 0, head
        while node:
            n += 1
            node = node.next
        size, extra = divmod(n, k)
        result = []
        node = head
        for i in range(k):
            result.append(node)
            length = size + (i < extra)
            if length:
                for _ in range(length - 1):
                    node = node.next
                node.next, node = None, node.next
        return result