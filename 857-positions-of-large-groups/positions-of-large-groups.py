
from typing import List

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        i = 0
        for j in range(len(s) + 1):
            if j == len(s) or s[j] != s[i]:
                if j - i >= 3:
                    res.append([i, j - 1])
                i = j
        return res
