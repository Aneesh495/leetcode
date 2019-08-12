
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Largest power of three within 32 bit signed range is 1162261467 which equals 3**19
        # If n divides this number evenly and n is positive then n is a power of three
        return n > 0 and 1162261467 % n == 0
