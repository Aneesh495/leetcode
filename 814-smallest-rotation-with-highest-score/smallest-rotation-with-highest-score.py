
from typing import List

class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        diff = [0] * (n + 1)
        
        base = 0
        for i, v in enumerate(nums):
            if v <= i:
                base += 1
            start = (i - v + 1) % n
            end = (i + 1) % n
            diff[start] -= 1
            diff[end] += 1
            if start > end:
                diff[0] -= 1
        
        best = 0
        max_score = base
        cur = base
        for k in range(1, n):
            cur += diff[k]
            if cur > max_score:
                max_score = cur
                best = k
        return best
