
from typing import List
from collections import defaultdict

class DSU:
    # Disjoint set union with path compression and union by size
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # path halving
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        # Sieve for smallest prime factor up to max value
        maxv = max(nums)
        spf = list(range(maxv + 1))
        p = 2
        while p * p <= maxv:
            if spf[p] == p:
                m = p * p
                while m <= maxv:
                    if spf[m] == m:
                        spf[m] = p
                    m += p
            p += 1

        # Factorize into unique prime factors using spf
        def prime_factors(x: int) -> List[int]:
            res = []
            last = 0
            while x > 1:
                f = spf[x]
                if f == 0:  # safety for x==1 which will not occur here
                    break
                if f != last:
                    res.append(f)
                    last = f
                x //= f
            return res

        n = len(nums)
        dsu = DSU(n)
        first_idx_by_prime = {}  # prime -> first index of nums that had this prime

        # Union indices that share any prime factor
        for i, a in enumerate(nums):
            for p in prime_factors(a):
                if p in first_idx_by_prime:
                    dsu.union(i, first_idx_by_prime[p])
                else:
                    first_idx_by_prime[p] = i

        # Count component sizes by root
        count = defaultdict(int)
        best = 0
        for i in range(n):
            r = dsu.find(i)
            count[r] += 1
            if count[r] > best:
                best = count[r]
        return best
