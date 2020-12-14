
from typing import List

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = []
        i = len(num) - 1
        carry = 0

        # Add from least significant digit using k's digits and carry
        while i >= 0 or k > 0 or carry:
            n = num[i] if i >= 0 else 0
            total = n + (k % 10) + carry
            res.append(total % 10)
            carry = total // 10
            k //= 10
            i -= 1

        return res[::-1]
