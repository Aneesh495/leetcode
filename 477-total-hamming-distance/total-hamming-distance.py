
from typing import List

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        # For each bit position count ones and zeros
        # Contribution of one bit is ones * zeros
        total = 0
        n = len(nums)
        for b in range(32):  # 32 bits cover given constraints
            ones = 0
            for x in nums:
                ones += (x >> b) & 1
            total += ones * (n - ones)
        return total
