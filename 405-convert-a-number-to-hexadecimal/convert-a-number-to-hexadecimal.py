
class Solution:
    def toHex(self, num: int) -> str:
        # Handle zero directly
        if num == 0:
            return "0"
        # Convert negatives to 32 bit two's complement
        num &= 0xFFFFFFFF
        digits = "0123456789abcdef"
        out = []
        # Extract 4 bits at a time
        while num:
            out.append(digits[num & 0xF])
            num >>= 4
        # Reverse to correct order
        return "".join(reversed(out))
