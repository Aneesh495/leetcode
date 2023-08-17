
from typing import List

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        """
        Count battleships in a 2D board in one pass with O(1) extra memory.
        A cell that starts a ship has no 'X' directly above and no 'X' directly to the left.
        Ships are placed only horizontally or vertically and never touch adjacent ships.
        """
        if not board or not board[0]:
            return 0

        rows = len(board)
        cols = len(board[0])
        count = 0

        for r in range(rows):
            for c in range(cols):
                # Skip empty water cells
                if board[r][c] != 'X':
                    continue

                # Check if there is an 'X' above
                has_up = r > 0 and board[r - 1][c] == 'X'
                # Check if there is an 'X' to the left
                has_left = c > 0 and board[r][c - 1] == 'X'

                # This cell is the head of a ship only if there is no 'X' above and no 'X' to the left
                if not has_up and not has_left:
                    count += 1

        return count
