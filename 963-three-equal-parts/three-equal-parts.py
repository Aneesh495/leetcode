
from typing import List

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        n = len(arr)
        total = sum(arr)
        if total == 0:
            return [0, n - 1]
        if total % 3 != 0:
            return [-1, -1]
        k = total // 3

        ones_pos = [i for i, v in enumerate(arr) if v == 1]
        i1 = ones_pos[0]
        i2 = ones_pos[k]
        i3 = ones_pos[2 * k]

        # Walk together to ensure the suffixes are identical
        while i3 < n:
            if arr[i1] != arr[i2] or arr[i2] != arr[i3]:
                return [-1, -1]
            i1 += 1
            i2 += 1
            i3 += 1

        return [i1 - 1, i2]
