from functools import cache

class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        mod = 1_000_000_007

        def count_through(bound: str) -> int:
            digits = [int(char) for char in bound]

            @cache
            def visit(pos: int, total: int, tight: bool) -> int:
                remaining = len(digits) - pos
                if total > max_sum or total + 9 * remaining < min_sum:
                    return 0
                if remaining == 0:
                    return 1
                upper = digits[pos] if tight else 9
                return sum(visit(pos + 1, total + digit, tight and digit == upper)
                           for digit in range(upper + 1)) % mod

            return visit(0, 0, True)

        # Both counts are inclusive. Add the lower endpoint back if it qualifies.
        lower_ok = min_sum <= sum(map(int, num1)) <= max_sum
        return (count_through(num2) - count_through(num1) + lower_ok) % mod