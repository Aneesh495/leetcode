
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Two pointers from both ends since input is nondecreasing
        # Largest square sits at either end
        n = len(nums)
        res = [0] * n
        i = n - 1
        l = 0
        r = n - 1

        while l <= r:
            left_sq = nums[l] * nums[l]
            right_sq = nums[r] * nums[r]
            if left_sq > right_sq:
                res[i] = left_sq
                l += 1
            else:
                res[i] = right_sq
                r -= 1
            i -= 1

        return res
