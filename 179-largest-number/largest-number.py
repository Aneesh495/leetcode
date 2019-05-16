
from typing import List
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert all numbers to strings so we can compare by concatenation
        s = list(map(str, nums))

        # Custom comparator
        # For any two strings a and b
        # a should come before b if ab is larger than ba
        def cmp(a: str, b: str) -> int:
            if a + b > b + a:
                return -1
            if a + b < b + a:
                return 1
            return 0

        s.sort(key=cmp_to_key(cmp))

        # Edge case where all numbers are zero
        if s[0] == "0":
            return "0"

        # Join to form the largest number
        return "".join(s)
