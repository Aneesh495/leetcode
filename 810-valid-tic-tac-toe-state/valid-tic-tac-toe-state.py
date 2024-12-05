
from typing import List

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        x = sum(r.count('X') for r in board)
        o = sum(r.count('O') for r in board)
        if not (x == o or x == o + 1):
            return False

        def win(p: str) -> bool:
            rows = any(all(board[r][c] == p for c in range(3)) for r in range(3))
            cols = any(all(board[r][c] == p for r in range(3)) for c in range(3))
            diags = all(board[i][i] == p for i in range(3)) or all(board[i][2 - i] == p for i in range(3))
            return rows or cols or diags

        xw = win('X')
        ow = win('O')

        if xw and ow:
            return False
        if xw and x != o + 1:
            return False
        if ow and x != o:
            return False
        return True
