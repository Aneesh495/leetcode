
from typing import List

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)

        for size in range(n, 1, -1):
            # Find index of the next max value 'size'
            idx = arr.index(size)
            if idx == size - 1:
                continue
            # Flip max to front if not already there
            if idx != 0:
                res.append(idx + 1)
                arr[:idx + 1] = reversed(arr[:idx + 1])
            # Flip it to its final position
            res.append(size)
            arr[:size] = reversed(arr[:size])

        return res
