
from typing import List

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        diff = [0] * (n + 1)        # diff[i] toggles active flip parity at i
        parity = 0                  # current flip parity at index i
        ans = 0

        for i in range(n):
            parity ^= diff[i]       # apply any flip ending/starting here
            if (nums[i] ^ parity) == 0:  # need to flip starting at i
                if i + k > n:
                    return -1
                ans += 1
                parity ^= 1
                diff[i + k] ^= 1    # flip effect ends at i + k

        return ans
