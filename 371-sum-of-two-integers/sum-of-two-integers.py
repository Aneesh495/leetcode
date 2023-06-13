
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Use 32-bit masking to simulate integer overflow behavior
        MASK = 0xffffffff          # 32 bits all 1s
        MAX_INT = 0x7fffffff       # Max positive 32-bit int

        # Iterate until there's no carry
        while b != 0:
            carry = (a & b) & MASK     # bits where both have 1s will carry
            a = (a ^ b) & MASK         # sum without carry
            b = (carry << 1) & MASK    # carry shifted left

        # If result is within positive range return as is
        # Otherwise convert from two's complement to Python negative
        return a if a <= MAX_INT else ~(a ^ MASK)
