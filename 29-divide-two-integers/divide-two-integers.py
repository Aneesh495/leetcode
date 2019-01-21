class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # guard the single overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # work with positive values
        a = abs(dividend)
        b = abs(divisor)
        q = 0

        # build quotient using shifts
        for bit in range(31, -1, -1):
            if (a >> bit) >= b:            # can fit b << bit into a
                a -= b << bit              # subtract that chunk
                q |= 1 << bit              # set the bit in q

        # apply sign
        if (dividend < 0) ^ (divisor < 0):
            q = -q

        # clamp to int range
        if q < INT_MIN:
            return INT_MIN
        if q > INT_MAX:
            return INT_MAX
        return q