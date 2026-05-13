import math

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def lcm(x: int, y: int) -> int:
            return x * y // math.gcd(x, y)

        ab = lcm(a, b)
        ac = lcm(a, c)
        bc = lcm(b, c)
        abc = lcm(ab, c)

        def count(x: int) -> int:
            return (
                x // a + x // b + x // c
                - x // ab - x // ac - x // bc
                + x // abc
            )

        left, right = 1, 2 * 10**9
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= n:
                right = mid
            else:
                left = mid + 1

        return left
