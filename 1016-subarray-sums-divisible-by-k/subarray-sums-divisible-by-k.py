
from typing import List
from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """
        Counts subarrays whose sum is divisible by k.
        Uses prefix sum modulo counting.
        Time O(n) Space O(k) in worst case.
        """
        count_by_mod = defaultdict(int)
        count_by_mod[0] = 1  # empty prefix has mod 0

        res = 0
        running_mod = 0

        for x in nums:
            # update running prefix modulo k
            running_mod = (running_mod + x) % k

            # any previous prefix with same mod forms a valid subarray
            res += count_by_mod[running_mod]

            # record current mod for future subarrays
            count_by_mod[running_mod] += 1

        return res
