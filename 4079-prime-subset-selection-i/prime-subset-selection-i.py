from math import isqrt

class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:
        limit = min(n, s)
        composite = bytearray(limit + 1)
        for p in range(2, isqrt(limit) + 1):
            if not composite[p]:
                composite[p * p : limit + 1 : p] = b'\x01' * ((limit - p * p) // p + 1)
        result = []
        # For any chosen count, the smallest primes have the minimum possible sum.
        for value in range(2, limit + 1):
            if not composite[value]:
                if value > s:
                    break
                result.append(value)
                s -= value
        return result