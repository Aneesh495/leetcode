class Solution:
    def alternateDigitSum(self, n: int) -> int:
        return sum((1 if i % 2 == 0 else -1) * int(c) for i, c in enumerate(str(n)))
