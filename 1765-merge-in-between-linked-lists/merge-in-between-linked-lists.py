class Solution:
    def mergeInBetween(self, list1, a, b, list2):
        before = list1
        for _ in range(a-1): before = before.next
        end = before
        for _ in range(b-a+2): end = end.next
        before.next = list2
        while list2.next: list2 = list2.next
        list2.next = end
        return list1