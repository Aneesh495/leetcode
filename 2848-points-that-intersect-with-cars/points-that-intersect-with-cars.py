class Solution:
    def numberOfPoints(self, nums: list[list[int]]) -> int:
        return len({x for s, e in nums for x in range(s, e + 1)})
