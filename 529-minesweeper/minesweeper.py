
from typing import List
from collections import deque

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # Reveal logic
        # If click hits a mine mark as X and return
        r, c = click
        rows, cols = len(board), len(board[0])
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board

        # Directions for 8 neighbors
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        # BFS flood fill starting from the clicked cell
        q = deque([(r, c)])
        seen = set([(r, c)])

        while q:
            i, j = q.popleft()
            if board[i][j] != 'E':
                # Already processed or revealed
                continue

            # Count adjacent mines and collect unrevealed empty neighbors
            mine_count = 0
            empties = []
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols:
                    if board[ni][nj] == 'M':
                        mine_count += 1
                    elif board[ni][nj] == 'E':
                        empties.append((ni, nj))

            if mine_count > 0:
                # Reveal number if any adjacent mine exists
                board[i][j] = str(mine_count)
            else:
                # Reveal blank and expand neighbors
                board[i][j] = 'B'
                for ni, nj in empties:
                    if (ni, nj) not in seen:
                        seen.add((ni, nj))
                        q.append((ni, nj))

        return board
