
from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        lo, hi = 0.0, 1.0
        while True:
            mid = (lo + hi) / 2
            count = 0
            i = -1
            p, q = 0, 1
            for j in range(1, n):
                while i + 1 < j and arr[i + 1] / arr[j] < mid:
                    i += 1
                    if arr[i] * q > arr[j] * p:
                        p, q = arr[i], arr[j]
                count += i + 1
            if count == k:
                return [p, q]
            if count < k:
                lo = mid
            else:
                hi = mid
