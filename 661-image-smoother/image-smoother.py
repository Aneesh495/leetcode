
from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        out = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                s = c = 0
                for r in range(max(0, i-1), min(m, i+2)):
                    for d in range(max(0, j-1), min(n, j+2)):
                        s += img[r][d]
                        c += 1
                out[i][j] = s // c
        return out
