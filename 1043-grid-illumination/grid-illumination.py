
from typing import List, Tuple, Dict, Set
from collections import defaultdict

class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        # Count maps for rows cols main diags and anti diags
        row = defaultdict(int)
        col = defaultdict(int)
        diag = defaultdict(int)      # r - c
        anti = defaultdict(int)      # r + c

        # Use a set to keep only one lamp per cell
        on: Set[Tuple[int, int]] = set()
        for r, c in lamps:
            if (r, c) in on:
                continue
            on.add((r, c))
            row[r] += 1
            col[c] += 1
            diag[r - c] += 1
            anti[r + c] += 1

        ans: List[int] = []
        # Directions for the cell and its eight neighbors
        dirs = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1),
                (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for r, c in queries:
            # Check illumination before turning off neighbors
            if row[r] > 0 or col[c] > 0 or diag[r - c] > 0 or anti[r + c] > 0:
                ans.append(1)
            else:
                ans.append(0)

            # Turn off any lamp at the cell or in the eight neighboring cells
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if (nr, nc) in on:
                    on.remove((nr, nc))
                    row[nr] -= 1
                    col[nc] -= 1
                    diag[nr - nc] -= 1
                    anti[nr + nc] -= 1

        return ans
