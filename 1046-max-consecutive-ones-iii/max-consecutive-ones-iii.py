
from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Sliding window that allows at most k zeros inside
        left = 0                          # Left edge of window
        zeros = 0                         # Count of zeros in current window
        best = 0                          # Best length seen

        for right, val in enumerate(nums):
            if val == 0:
                zeros += 1                # We include a zero and spend one flip

            # If we exceeded k flips then move left forward
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1            # We discard a zero so refund one flip
                left += 1                 # Shrink window from the left

            # Window [left, right] is valid so update best
            best = max(best, right - left + 1)

        return best
