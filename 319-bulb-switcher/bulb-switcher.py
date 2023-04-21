
from math import isqrt

class Solution:
    def bulbSwitch(self, n: int) -> int:
        # A bulb ends on only if toggled an odd number of times
        # Bulb i is toggled once per divisor of i
        # Only perfect squares have an odd count of divisors
        # So the answer is the count of perfect squares up to n
        return isqrt(n)
