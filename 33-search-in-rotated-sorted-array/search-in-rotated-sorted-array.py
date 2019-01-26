
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Classic binary search adapted for a rotated sorted array
        # At each step one side is sorted and the other side is rotated
        # Decide which side is sorted then check if the target lies inside it

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            # Left half is sorted
            if nums[l] <= nums[m]:
                # Target inside the sorted left half
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                # Right half is sorted
                # Target inside the sorted right half
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1