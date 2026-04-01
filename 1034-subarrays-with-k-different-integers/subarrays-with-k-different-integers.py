
from typing import List
from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # Count subarrays with exactly k distinct values
        # Use the identity: exactly(k) = at_most(k) - at_most(k - 1)
        return self._at_most(nums, k) - self._at_most(nums, k - 1)

    def _at_most(self, nums: List[int], k: int) -> int:
        # Sliding window counting subarrays with at most k distinct values
        if k < 0:
            return 0

        freq = defaultdict(int)     # frequency of values in the current window
        left = 0                    # left bound of window
        distinct = 0                # count of distinct values in window
        total = 0                   # total subarrays with at most k distinct

        for right, val in enumerate(nums):
            # expand window to include nums[right]
            if freq[val] == 0:
                distinct += 1
            freq[val] += 1

            # shrink window until distinct <= k
            while distinct > k:
                drop = nums[left]
                freq[drop] -= 1
                if freq[drop] == 0:
                    distinct -= 1
                left += 1

            # all subarrays ending at right with left..right are valid
            total += right - left + 1

        return total
