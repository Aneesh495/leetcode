
from typing import List

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # locate the rook
        r = c = -1
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    r, c = i, j
                    break
            if r != -1:
                break

        # scan in four directions and count the first pawn seen before any bishop
        captures = 0
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            x, y = r + dr, c + dc
            while 0 <= x < 8 and 0 <= y < 8:
                cell = board[x][y]
                if cell == 'B':
                    break
                if cell == 'p':
                    captures += 1
                    break
                x += dr
                y += dc
        return captures
