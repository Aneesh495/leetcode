from collections import Counter
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        c = Counter(nums)
        if 1 in c.values():
            return -1
        return sum((v + 2) // 3 for v in c.values())
