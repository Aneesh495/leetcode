
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Track seen digits for each row each column and each 3x3 box
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]  # box index is (r // 3) * 3 + (c // 3)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue  # skip empty cells
                b = (r // 3) * 3 + (c // 3)

                # If digit already present in its row or column or box it is invalid
                if val in rows[r] or val in cols[c] or val in boxes[b]:
                    return False

                # Record the digit as seen
                rows[r].add(val)
                cols[c].add(val)
                boxes[b].add(val)

        # No conflicts found
        return True