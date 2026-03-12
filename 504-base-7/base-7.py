
class Solution:
    def convertToBase7(self, num: int) -> str:
        # Handle zero early since loop below would skip and we must return "0"
        if num == 0:
            return "0"

        # Track sign then work with absolute value
        sign = "-" if num < 0 else ""
        n = abs(num)

        # Repeated division by 7 collects digits in reverse order
        digits = []
        while n > 0:
            digits.append(str(n % 7))   # push remainder digit
            n //= 7                     # reduce n

        # Reverse digits to correct order and prefix sign if needed
        return sign + "".join(reversed(digits))
