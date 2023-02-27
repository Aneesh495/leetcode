
class Solution:
    def addDigits(self, num: int) -> int:
        # Digital root in O(1)
        # For num == 0 the result is 0
        # Otherwise the result cycles every 9: 1 + (num - 1) % 9
        return 0 if num == 0 else 1 + (num - 1) % 9
