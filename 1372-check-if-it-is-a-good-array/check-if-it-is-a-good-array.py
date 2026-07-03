from typing import List
from math import gcd

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        g = 0
        for num in nums:
            g = gcd(g, num)
        return g == 1
