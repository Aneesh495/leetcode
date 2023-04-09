
from typing import List

class NumArray:
    # Fenwick tree solution
    # Time
    #   update O(log n)
    #   sumRange O(log n)
    def __init__(self, nums: List[int]):
        # copy original values to track deltas on update
        self.arr = nums[:]
        self.n = len(nums)
        # internal BIT uses 1 based indexing
        self.bit = [0] * (self.n + 1)
        # build BIT in O(n log n)
        for i, v in enumerate(nums, 1):
            self._add(i, v)

    def _add(self, i: int, delta: int) -> None:
        # add delta to index i and propagate upward
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def _prefix(self, i: int) -> int:
        # sum of [1..i] in BIT
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def update(self, index: int, val: int) -> None:
        # compute change then apply to BIT
        delta = val - self.arr[index]
        self.arr[index] = val
        self._add(index + 1, delta)

    def sumRange(self, left: int, right: int) -> int:
        # sum [left..right] equals prefix(right) minus prefix(left - 1)
        return self._prefix(right + 1) - self._prefix(left)
