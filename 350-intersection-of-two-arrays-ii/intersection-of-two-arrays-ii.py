
from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Return the multiset intersection of nums1 and nums2.
        Time O(n + m) where n = len(nums1) and m = len(nums2)
        Space O(min(n, m)) since we count only the smaller array
        """
        # Always count the smaller array to minimize memory
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        counts = Counter(nums1)
        out: List[int] = []

        # For each number in the other array
        # emit it if we still have remaining count
        for x in nums2:
            c = counts.get(x, 0)
            if c:
                out.append(x)
                if c == 1:
                    # Drop key to keep the dict tight
                    counts.pop(x)
                else:
                    counts[x] = c - 1

        return out
