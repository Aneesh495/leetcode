
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Handle non positive values first
        # A power of two has exactly one set bit in binary
        # For such n the expression n & (n - 1) equals zero
        return n > 0 and (n & (n - 1)) == 0
