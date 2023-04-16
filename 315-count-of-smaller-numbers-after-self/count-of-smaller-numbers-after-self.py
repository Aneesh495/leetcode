
from typing import List

class Fenwick:
    # Binary Indexed Tree supporting point updates and prefix sums
    def __init__(self, size: int):
        self.n = size
        self.bit = [0] * (self.n + 1)

    def update(self, i: int, delta: int) -> None:
        # add delta at index i
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def query(self, i: int) -> int:
        # sum from 1 to i inclusive
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # coordinate compress values to 1..m to keep Fenwick size small
        vals = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(vals)}
        bit = Fenwick(len(vals))
        ans = []
        # iterate from right to left
        for v in reversed(nums):
            i = rank[v]
            # count of elements strictly smaller to the right
            ans.append(bit.query(i - 1))
            bit.update(i, 1)
        return ans[::-1]
