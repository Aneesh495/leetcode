
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Classic binary search on a sorted list with distinct integers
        # We keep an invariant that the answer is in [lo, hi] as an insertion point
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            # If mid value is less than target then answer is to the right of mid
            if nums[mid] < target:
                lo = mid + 1
            else:
                # nums[mid] is greater than or equal to target so answer is at mid or to the left
                hi = mid
        # lo is the first index with value greater than or equal to target
        # This is the found index if target exists otherwise the insert position
        return lo