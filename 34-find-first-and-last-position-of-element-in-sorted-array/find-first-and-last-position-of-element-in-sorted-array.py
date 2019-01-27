
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Find first index i where nums[i] >= target
        def lower_bound(a: List[int], x: int) -> int:
            lo = 0
            hi = len(a)
            # Invariant. All indices < lo are < x. All indices >= hi are >= x.
            while lo < hi:
                mid = (lo + hi) // 2
                if a[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo  # First index with value >= x. May be len(a)
        
        # Find first index i where nums[i] > target
        def upper_bound(a: List[int], x: int) -> int:
            lo = 0
            hi = len(a)
            # Invariant. All indices < lo are <= x. All indices >= hi are > x.
            while lo < hi:
                mid = (lo + hi) // 2
                if a[mid] <= x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo  # First index with value > x. May be len(a)
        
        if not nums:
            return [-1, -1]
        
        left = lower_bound(nums, target)
        # If left is out of range or the value at left is not target then target is absent
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        
        right = upper_bound(nums, target) - 1
        return [left, right]