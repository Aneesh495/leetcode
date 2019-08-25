
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Must be positive
        # Must be a power of two -> only one bit set
        # That bit must be in an even index position -> mask 0x55555555 keeps bits 0,2,4,...
        return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0
