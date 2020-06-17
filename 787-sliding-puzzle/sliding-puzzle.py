
from collections import deque
from typing import List

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = ''.join(str(x) for row in board for x in row)
        target = '123450'
        if start == target:
            return 0

        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }

        q = deque([(start, start.index('0'), 0)])
        seen = {start}

        while q:
            state, z, dist = q.popleft()
            for nz in neighbors[z]:
                s_list = list(state)
                s_list[z], s_list[nz] = s_list[nz], s_list[z]
                nxt = ''.join(s_list)
                if nxt == target:
                    return dist + 1
                if nxt not in seen:
                    seen.add(nxt)
                    q.append((nxt, nz, dist + 1))
        return -1
