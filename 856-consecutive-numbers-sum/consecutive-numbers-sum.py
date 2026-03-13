
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        while n % 2 == 0:
            n //= 2
        res = 1
        p = 3
        while p * p <= n:
            cnt = 0
            while n % p == 0:
                n //= p
                cnt += 1
            if cnt:
                res *= (cnt + 1)
            p += 2
        if n > 1:
            res *= 2
        return res
