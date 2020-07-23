
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        s = set(nums)
        res = 0
        cur = head
        while cur:
            if cur.val in s and (cur.next is None or cur.next.val not in s):
                res += 1
            cur = cur.next
        return res
