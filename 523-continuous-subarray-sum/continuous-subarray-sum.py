
from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # If k is 0 then we need a subarray of length at least 2 whose sum is 0
        # With nonnegative nums this only happens if there are two consecutive zeros
        if k == 0:
            for i in range(len(nums) - 1):
                if nums[i] == 0 and nums[i + 1] == 0:
                    return True
            return False

        # Normalize k to be positive for modulo operations
        if k < 0:
            k = -k

        # Map remainder -> earliest index where this remainder occurred
        # Seed with remainder 0 at index -1 so a prefix itself can form a valid subarray
        first_idx = {0: -1}
        prefix_mod = 0

        for i, x in enumerate(nums):
            prefix_mod = (prefix_mod + x) % k  # current prefix sum modulo k

            if prefix_mod in first_idx:
                # Subarray length at least 2
                if i - first_idx[prefix_mod] >= 2:
                    return True
            else:
                # Store earliest index for this remainder
                first_idx[prefix_mod] = i

        return False
