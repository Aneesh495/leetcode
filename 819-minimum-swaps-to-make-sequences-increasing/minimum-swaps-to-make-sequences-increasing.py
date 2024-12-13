
from typing import List

class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        keep, swap = 0, 1
        for i in range(1, n):
            nk = ns = float('inf')
            if nums1[i-1] < nums1[i] and nums2[i-1] < nums2[i]:
                nk = min(nk, keep)
                ns = min(ns, swap + 1)
            if nums1[i-1] < nums2[i] and nums2[i-1] < nums1[i]:
                nk = min(nk, swap)
                ns = min(ns, keep + 1)
            keep, swap = nk, ns
        return min(keep, swap)
