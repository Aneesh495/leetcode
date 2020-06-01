
from typing import List

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        pos = {p: i for i, p in enumerate(row)}
        swaps = 0
        for i in range(0, len(row), 2):
            a = row[i]
            b = a ^ 1
            if row[i + 1] != b:
                j = pos[b]
                pos[row[i + 1]] = j
                row[j], row[i + 1] = row[i + 1], row[j]
                pos[b] = i + 1
                swaps += 1
        return swaps
