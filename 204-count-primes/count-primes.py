
from typing import List

class Solution:
    def countPrimes(self, n: int) -> int:
        # Count primes strictly less than n using Sieve of Eratosthenes
        if n <= 2:
            return 0

        # Initialize primality array of size n
        # Index i represents number i
        is_prime: List[bool] = [True] * n
        is_prime[0] = False
        is_prime[1] = False

        # Only need to sieve with bases up to sqrt(n)
        limit = int(n ** 0.5) + 1

        for i in range(2, limit):
            if is_prime[i]:
                # Start crossing off from i*i since smaller multiples already handled
                start = i * i
                step = i
                # Mark all multiples of i as not prime
                # The slice length is computed so the assignment fits exactly
                if start < n:
                    is_prime[start:n:step] = [False] * (((n - 1 - start) // step) + 1)

        # Count remaining True entries
        return sum(is_prime)
