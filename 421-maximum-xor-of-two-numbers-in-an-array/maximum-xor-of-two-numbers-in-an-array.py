from typing import List

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_bit = max(nums).bit_length()
        res = 0
        mask = 0
        for bit in range(max_bit - 1, -1, -1):
            mask |= 1 << bit
            prefixes = {n & mask for n in nums}
            candidate = res | (1 << bit)
            if any((candidate ^ p) in prefixes for p in prefixes):
                res = candidate
        return res
