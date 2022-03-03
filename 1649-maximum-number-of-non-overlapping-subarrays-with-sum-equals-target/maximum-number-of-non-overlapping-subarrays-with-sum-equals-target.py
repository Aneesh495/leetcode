class Solution:
    def maxNonOverlapping(self, nums: list[int], target: int) -> int:
        seen = {0}
        total = ans = 0
        for x in nums:
            total += x
            if total-target in seen:
                ans += 1
                total = 0
                seen = {0}
            else: seen.add(total)
        return ans