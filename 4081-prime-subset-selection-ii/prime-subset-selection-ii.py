from math import isqrt

class Solution:
    def maxPrimeSubset(self, n: int, s: int) -> list[int]:
        bound = min(n, s)
        composite = bytearray(bound + 1)
        for p in range(2, isqrt(bound) + 1):
            if not composite[p]:
                composite[p * p : bound + 1 : p] = b'\x01' * ((bound - p * p) // p + 1)
        primes = [p for p in range(2, bound + 1) if not composite[p]]
        impossible = s + 1
        dp = [[impossible] * (s + 1) for _ in range(len(primes) + 1)]
        dp[-1][0] = 0
        for i in range(len(primes) - 1, -1, -1):
            prime = primes[i]
            dp[i][:] = dp[i + 1]
            for total in range(prime, s + 1):
                dp[i][total] = min(dp[i][total], 1 + dp[i + 1][total - prime])

        remaining = s
        while dp[0][remaining] == impossible:
            remaining -= 1
        result = []
        # Prefer the earliest prime whenever it preserves the optimal number of choices.
        for i, prime in enumerate(primes):
            if prime <= remaining and dp[i][remaining] == 1 + dp[i + 1][remaining - prime]:
                result.append(prime)
                remaining -= prime
            if remaining == 0:
                break
        return result