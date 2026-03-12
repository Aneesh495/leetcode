
from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # Binary search using index parity
        # Pairs start at even indices before the single element
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            # Ensure mid is even to compare pairs cleanly
            if mid % 2 == 1:
                mid -= 1
            # If pair matches, single is to the right of mid+1
            if nums[mid] == nums[mid + 1]:
                lo = mid + 2
            else:
                hi = mid
        return nums[lo]
