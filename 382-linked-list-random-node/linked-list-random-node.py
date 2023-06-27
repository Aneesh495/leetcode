
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional
import random

class Solution:
    # Store the head pointer so we can traverse the list on each query
    def __init__(self, head: Optional['ListNode']):
        self.head = head

    def getRandom(self) -> int:
        # Reservoir sampling of size 1
        # Walk the list once
        # Replace the chosen value with probability 1/i at the i-th node
        # This gives each node equal probability without extra space
        ans = None
        i = 1
        node = self.head
        while node:
            if random.randrange(i) == 0:
                ans = node.val
            i += 1
            node = node.next
        return ans
