
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # Fill the board in place using backtracking
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        for r in range(9):
            for c in range(9):
                ch = board[r][c]
                if ch == '.':
                    empties.append((r, c))
                else:
                    rows[r].add(ch)
                    cols[c].add(ch)
                    boxes[(r // 3) * 3 + c // 3].add(ch)

        def backtrack(i: int = 0) -> bool:
            if i == len(empties):
                return True
            r, c = empties[i]
            b = (r // 3) * 3 + c // 3
            for d in map(str, range(1, 10)):
                if d not in rows[r] and d not in cols[c] and d not in boxes[b]:
                    board[r][c] = d
                    rows[r].add(d)
                    cols[c].add(d)
                    boxes[b].add(d)
                    if backtrack(i + 1):
                        return True
                    rows[r].remove(d)
                    cols[c].remove(d)
                    boxes[b].remove(d)
                    board[r][c] = '.'
            return False

        backtrack()