class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        zero = nums.index(0)
        ascending = all((nums[(i + 1) % n] - nums[i]) % n == 1 % n for i in range(n))
        descending = all((nums[i] - nums[(i + 1) % n]) % n == 1 % n for i in range(n))
        best = n + 3
        if ascending:
            # Two reversals can turn left rotations into shorter right rotations.
            best = min(best, zero, n - zero + 2)
        if descending:
            # With one reversal, rotate before it or after it, whichever is cheaper.
            best = min(best, 1 + (zero + 1) % n, n - zero)
        return -1 if best == n + 3 else best