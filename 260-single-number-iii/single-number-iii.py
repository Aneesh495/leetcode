
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # xor of all numbers equals a xor b where a and b are the two unique numbers
        all_xor = 0
        for v in nums:
            all_xor ^= v

        # isolate a set bit that differs between a and b
        mask = all_xor & -all_xor

        # partition numbers by that bit and xor within each group to recover a and b
        a = 0
        b = 0
        for v in nums:
            if v & mask:
                a ^= v
            else:
                b ^= v

        return [a, b]
