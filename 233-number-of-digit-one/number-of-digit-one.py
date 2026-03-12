
class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        res = 0
        m = 1
        while m <= n:
            high = n // (m * 10)
            cur = (n // m) % 10
            low = n % m
            if cur == 0:
                res += high * m
            elif cur == 1:
                res += high * m + low + 1
            else:
                res += (high + 1) * m
            m *= 10
        return res
