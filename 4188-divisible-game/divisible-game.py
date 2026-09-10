from collections import defaultdict
from itertools import accumulate

class Solution:
    def divisibleGame(self, nums: list[int]) -> int:
        prefix = list(accumulate(nums, initial=0))
        factors = defaultdict(list)
        cache = {}
        for index, value in enumerate(nums):
            if value not in cache:
                primes = []
                x = value
                p = 2
                while p * p <= x:
                    if x % p == 0:
                        primes.append(p)
                        while x % p == 0:
                            x //= p
                    p += 1
                if x > 1:
                    primes.append(x)
                cache[value] = primes
            for prime in cache[value]:
                factors[prime].append(index)

        best, chosen = -min(nums), 2
        for prime, indices in factors.items():
            previous = -1
            running = 0
            for index in indices:
                negatives = prefix[index] - prefix[previous + 1]
                running = max(nums[index], running + nums[index] - negatives)
                if running > best or (running == best and prime < chosen):
                    best, chosen = running, prime
                previous = index
        # Every composite divisor is dominated by one of its smaller prime factors.
        return best * chosen % 1_000_000_007