
# LeetCode 372. Super Pow
# Recurrence: a^(b1...bn) mod M = (a^(b1...b(n-1)) mod M)^10 * a^bn mod M
# Compute with fast modular exponentiation and process digits from the end

from typing import List

class Solution:
    MOD = 1337

    def _mod_pow(self, a: int, k: int) -> int:
        a %= self.MOD
        res = 1
        while k:
            if k & 1:
                res = (res * a) % self.MOD
            a = (a * a) % self.MOD
            k //= 2
        return res

    def superPow(self, a: int, b: List[int]) -> int:
        if not b:
            return 1
        last = b.pop()
        part1 = self._mod_pow(self.superPow(a, b), 10)
        part2 = self._mod_pow(a, last)
        return (part1 * part2) % self.MOD
