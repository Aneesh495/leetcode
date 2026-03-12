
from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # Handle empty input
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        res = [0] * (m * n)
        
        r = 0
        c = 0
        up = True  # True means moving up right. False means moving down left.
        
        for i in range(m * n):
            res[i] = mat[r][c]
            
            if up:
                # If at last column, go down and flip direction
                if c == n - 1:
                    r += 1
                    up = False
                # If at first row, go right and flip direction
                elif r == 0:
                    c += 1
                    up = False
                else:
                    r -= 1
                    c += 1
            else:
                # If at last row, go right and flip direction
                if r == m - 1:
                    c += 1
                    up = True
                # If at first column, go down and flip direction
                elif c == 0:
                    r += 1
                    up = True
                else:
                    r += 1
                    c -= 1
        
        return res
