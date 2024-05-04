class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        s = set()
        for i, x in enumerate(reversed(nums), 1):
            if x <= k:
                s.add(x)
                if len(s) == k:
                    return i
        return len(nums)
