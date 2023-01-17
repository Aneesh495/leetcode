
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Maintain a set for the current window of at most k indices
        seen = set()
        left = 0

        for right, val in enumerate(nums):
            # If value already in window then indices are within k
            if val in seen:
                return True

            # Add current value to window
            seen.add(val)

            # Shrink window to keep size at most k
            if right - left >= k:
                seen.remove(nums[left])
                left += 1

        return False
