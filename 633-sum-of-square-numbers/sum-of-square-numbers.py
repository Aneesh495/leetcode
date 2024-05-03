
from math import isqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, isqrt(c)
        while a <= b:
            s = a * a + b * b
            if s == c:
                return True
            if s > c:
                b -= 1
            else:
                a += 1
        return False
