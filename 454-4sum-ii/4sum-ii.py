
from typing import List
from collections import Counter

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # Count all pair sums from nums1 and nums2
        ab_counts = Counter()
        for a in nums1:
            for b in nums2:
                ab_counts[a + b] += 1

        # For each pair sum in nums3 and nums4, add matches that complete sum to 0
        total = 0
        for c in nums3:
            for d in nums4:
                total += ab_counts.get(-(c + d), 0)

        # Time O(n^2) space O(n^2)
        return total
