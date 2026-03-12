
from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board)
        n = len(board[0]) if m else 0
        dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for i in range(m):
            for j in range(n):
                live = 0
                for di, dj in dirs:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < m and 0 <= nj < n and abs(board[ni][nj]) == 1:
                        live += 1
                if board[i][j] == 1 and (live < 2 or live > 3):
                    board[i][j] = -1
                elif board[i][j] == 0 and live == 3:
                    board[i][j] = 2
        for i in range(m):
            for j in range(n):
                board[i][j] = 1 if board[i][j] > 0 else 0
