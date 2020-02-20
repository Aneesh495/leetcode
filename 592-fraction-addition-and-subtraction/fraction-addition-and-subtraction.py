
from math import gcd

class Solution:
    def fractionAddition(self, expression: str) -> str:
        i, n = 0, len(expression)
        num, den = 0, 1  # running fraction

        while i < n:
            sign = 1
            if expression[i] in '+-':
                sign = -1 if expression[i] == '-' else 1
                i += 1

            # parse numerator
            j = i
            while expression[j] != '/':
                j += 1
            n1 = int(expression[i:j]) * sign
            i = j + 1

            # parse denominator
            j = i
            while j < n and expression[j] not in '+-':
                j += 1
            d1 = int(expression[i:j])
            i = j

            # add to running result
            num = num * d1 + n1 * den
            den = den * d1
            g = gcd(abs(num), den)
            num //= g
            den //= g

        return f"{num}/{den}"
