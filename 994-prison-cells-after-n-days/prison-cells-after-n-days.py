
from typing import List

class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        # Use cycle detection since states repeat
        # Key is the tuple of eight cells
        seen = {}
        while n > 0:
            state = tuple(cells)
            if state in seen:
                # We have a cycle
                cycle_len = seen[state] - n
                n %= cycle_len
            seen[state] = n
            if n == 0:
                break
            n -= 1
            nxt = [0] * 8
            for i in range(1, 7):
                nxt[i] = 1 if cells[i - 1] == cells[i + 1] else 0
            cells = nxt
        return cells
