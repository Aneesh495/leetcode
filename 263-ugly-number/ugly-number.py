
class Solution:
    def isUgly(self, n: int) -> bool:
        # Ugly numbers have no prime factors other than 2 3 5
        # Edge case
        if n <= 0:
            return False

        # Repeatedly divide out factors 2 3 5
        for p in (2, 3, 5):
            while n % p == 0:
                n //= p

        # If all factors were 2 3 5 the remainder becomes 1
        return n == 1
