from typing import List
from collections import deque

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # state: (r, c, d)
        # d = 0 -> horizontal, snake occupies (r, c) and (r, c+1)
        # d = 1 -> vertical,   snake occupies (r, c) and (r+1, c)
        q = deque([(0, 0, 0, 0)])  # r, c, d, steps
        seen = {(0, 0, 0)}

        while q:
            r, c, d, steps = q.popleft()

            if r == n - 1 and c == n - 2 and d == 0:
                return steps

            if d == 0:
                # move right
                if c + 2 < n and grid[r][c + 2] == 0:
                    state = (r, c + 1, 0)
                    if state not in seen:
                        seen.add(state)
                        q.append((r, c + 1, 0, steps + 1))

                # move down
                if r + 1 < n and grid[r + 1][c] == 0 and grid[r + 1][c + 1] == 0:
                    state = (r + 1, c, 0)
                    if state not in seen:
                        seen.add(state)
                        q.append((r + 1, c, 0, steps + 1))

                    # rotate clockwise to vertical
                    state = (r, c, 1)
                    if state not in seen:
                        seen.add(state)
                        q.append((r, c, 1, steps + 1))

            else:
                # move down
                if r + 2 < n and grid[r + 2][c] == 0:
                    state = (r + 1, c, 1)
                    if state not in seen:
                        seen.add(state)
                        q.append((r + 1, c, 1, steps + 1))

                # move right
                if c + 1 < n and grid[r][c + 1] == 0 and grid[r + 1][c + 1] == 0:
                    state = (r, c + 1, 1)
                    if state not in seen:
                        seen.add(state)
                        q.append((r, c + 1, 1, steps + 1))

                    # rotate counterclockwise to horizontal
                    state = (r, c, 0)
                    if state not in seen:
                        seen.add(state)
                        q.append((r, c, 0, steps + 1))

        return -1
