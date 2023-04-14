
from typing import List

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # Dynamic programming with multiple pointers
        # uglies[i] stores the i-th super ugly number
        uglies = [1] * n

        k = len(primes)
        # idx[j] points to the position in uglies whose value times primes[j] is the next candidate
        idx = [0] * k
        # vals[j] is the current candidate value for primes[j]
        vals = primes[:]  # primes[j] * uglies[idx[j]]

        for i in range(1, n):
            # next number is the minimum candidate
            next_ugly = min(vals)
            uglies[i] = next_ugly

            # advance all pointers that match the chosen minimum
            for j in range(k):
                if vals[j] == next_ugly:
                    idx[j] += 1
                    vals[j] = primes[j] * uglies[idx[j]]

        return uglies[-1]
