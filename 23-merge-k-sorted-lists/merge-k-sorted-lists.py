
# Definition for singly-linked list is provided by LeetCode
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import List, Optional
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Use a min heap to always pull the smallest available node
        # Heap entries are tuples to break ties deterministically
        # Tuple layout is (node value, list index, node reference)
        heap = []
        for i, node in enumerate(lists):
            if node is not None:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        tail = dummy

        # Repeatedly pop the smallest node and push its successor
        while heap:
            val, i, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next is not None:
                heapq.heappush(heap, (node.next.val, i, node.next))

        tail.next = None
        # Total nodes processed N
        # Time O(N log k) where k is number of lists
        # Space O(k) for the heap
        return dummy.next