
from typing import List

class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        # validity check using XOR condition
        for i in range(n):
            for j in range(n):
                if board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]:
                    return -1

        rowSum = sum(board[0])
        colSum = sum(board[i][0] for i in range(n))
        if not (n // 2 <= rowSum <= (n + 1) // 2):
            return -1
        if not (n // 2 <= colSum <= (n + 1) // 2):
            return -1

        rowSwap = sum(board[i][0] == i % 2 for i in range(n))
        colSwap = sum(board[0][i] == i % 2 for i in range(n))

        if n % 2:
            if rowSwap % 2:
                rowSwap = n - rowSwap
            if colSwap % 2:
                colSwap = n - colSwap
        else:
            rowSwap = min(rowSwap, n - rowSwap)
            colSwap = min(colSwap, n - colSwap)

        return (rowSwap + colSwap) // 2
