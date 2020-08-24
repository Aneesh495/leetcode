
from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        total = 0
        res = []
        for i in range(len(s) - 1, -1, -1):
            total = (total + shifts[i]) % 26
            res.append(chr((ord(s[i]) - 97 + total) % 26 + 97))
        return "".join(reversed(res))
