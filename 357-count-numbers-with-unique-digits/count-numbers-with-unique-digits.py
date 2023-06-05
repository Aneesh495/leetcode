
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # Count numbers in [0, 10^n) with all digits unique
        # Edge case for n == 0
        if n == 0:
            return 1

        # For n >= 1 start with 10 for n == 1 (0 through 9)
        ans = 10
        # unique counts numbers with unique digits for current length
        unique = 9  # first digit choices for length >= 1
        available = 9  # remaining digit choices for subsequent positions

        # Build counts for lengths 2 to n
        # There are only 10 unique digits, so cap at 10
        for _ in range(2, min(n, 10) + 1):
            unique *= available  # multiply choices for next position
            ans += unique
            available -= 1

        return ans
