
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Map each value in nums2 to its next greater element using a monotonic stack
        next_greater = {}                 # value -> next greater value
        stack = []                        # decreasing stack of values

        for x in nums2:
            # Resolve next greater for any smaller values waiting on the stack
            while stack and x > stack[-1]:
                smaller = stack.pop()
                next_greater[smaller] = x
            stack.append(x)

        # Any values left on the stack have no next greater element
        while stack:
            next_greater[stack.pop()] = -1

        # Build the answer for nums1 by lookup
        return [next_greater[v] for v in nums1]
