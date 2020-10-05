
class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i - 1] << 1) % MOD
        res = 0
        for i, x in enumerate(nums):
            res = (res + x * (pow2[i] - pow2[n - 1 - i])) % MOD
        return res
