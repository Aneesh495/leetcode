class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10**9 + 7

        def count_primes(n: int) -> int:
            count = 0
            for x in range(2, n + 1):
                is_prime = True
                d = 2
                while d * d <= x:
                    if x % d == 0:
                        is_prime = False
                        break
                    d += 1
                if is_prime:
                    count += 1
            return count

        primes = count_primes(n)
        non_primes = n - primes

        ans = 1
        for i in range(2, primes + 1):
            ans = (ans * i) % MOD
        for i in range(2, non_primes + 1):
            ans = (ans * i) % MOD

        return ans
