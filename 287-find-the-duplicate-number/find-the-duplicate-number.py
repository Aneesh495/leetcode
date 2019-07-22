
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1 find intersection inside the cycle using Floyd's Tortoise and Hare
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]              # move one step
            fast = nums[nums[fast]]        # move two steps
            if slow == fast:
                break

        # Phase 2 find the cycle entrance which is the duplicate number
        ptr1 = nums[0]
        ptr2 = slow
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]

        return ptr1
