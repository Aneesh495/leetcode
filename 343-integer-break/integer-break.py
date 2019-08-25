
class Solution:
    def integerBreak(self, n: int) -> int:
        """
        Max product by splitting n into at least two positive integers.
        Key fact:
          The product is maximized by using as many 3s as possible.
          Special case when remainder is 1. Convert 3 + 1 into 2 + 2.
        Edge cases:
          n == 2 -> 1  because 1 + 1 product 1
          n == 3 -> 2  because 2 + 1 product 2
        """
        if n == 2:
            return 1
        if n == 3:
            return 2

        # Use as many 3s as possible
        count_three = n // 3
        rem = n % 3

        # If remainder is 0. Answer is 3^count_three
        if rem == 0:
            return 3 ** count_three

        # If remainder is 1. Replace one 3 with two 2s
        # So product becomes 3^(count_three - 1) * 4
        if rem == 1:
            return (3 ** (count_three - 1)) * 4

        # If remainder is 2. Multiply by 2 at the end
        return (3 ** count_three) * 2
