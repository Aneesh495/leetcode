# Definition for singly linked list node used by LeetCode
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy head to simplify pointer handling
        dummy = ListNode(0)
        tail = dummy  # Tail always points to the last node in the merged list

        # Walk both lists and always append the smaller current node to tail
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1      # Link tail to list1 current
                list1 = list1.next     # Advance list1
            else:
                tail.next = list2      # Link tail to list2 current
                list2 = list2.next     # Advance list2
            tail = tail.next           # Advance tail to the newly added node

        # One of the lists may still have nodes
        # Link the remainder directly since both lists are already sorted
        tail.next = list1 if list1 else list2

        # The merged list starts at dummy.next
        return dummy.next