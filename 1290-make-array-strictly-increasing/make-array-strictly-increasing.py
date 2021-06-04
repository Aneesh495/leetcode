from typing import List
from bisect import bisect_right


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(set(arr2))
        dp = {-1: 0}  # last_value -> min operations

        for x in arr1:
            ndp = {}

            for prev, ops in dp.items():
                if x > prev:
                    if x not in ndp or ops < ndp[x]:
                        ndp[x] = ops

                i = bisect_right(arr2, prev)
                if i < len(arr2):
                    y = arr2[i]
                    if y not in ndp or ops + 1 < ndp[y]:
                        ndp[y] = ops + 1

            if not ndp:
                return -1

            dp = ndp

        return min(dp.values())

