
import math

class Solution:
    def numSquares(self, n: int) -> int:
        while n % 4 == 0:
            n //= 4
        if n % 8 == 7:
            return 4
        if int(math.isqrt(n)) ** 2 == n:
            return 1
        r = int(math.isqrt(n))
        for i in range(1, r + 1):
            if int(math.isqrt(n - i * i)) ** 2 == n - i * i:
                return 2
        return 3
