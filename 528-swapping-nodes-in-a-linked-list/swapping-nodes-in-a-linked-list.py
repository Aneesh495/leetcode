class Solution:
    def swapNodes(self, head, k):
        a=head
        for _ in range(k-1): a=a.next
        b=head; p=a
        while p.next: p=p.next; b=b.next
        a.val,b.val=b.val,a.val
        return head