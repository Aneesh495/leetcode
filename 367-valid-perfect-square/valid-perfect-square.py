
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Handle 0 and 1 early
        if num < 2:
            return True

        # Binary search between 2 and num // 2
        left = 2
        right = num // 2

        while left <= right:
            mid = (left + right) // 2
            sq = mid * mid

            if sq == num:
                return True
            elif sq < num:
                left = mid + 1
            else:
                right = mid - 1

        return False
