
from typing import List

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [0] * (n + 1)
        ans = 0
        for i in range(1, m + 1):
            prev = 0
            for j in range(1, n + 1):
                temp = dp[j]
                if nums1[i - 1] == nums2[j - 1]:
                    dp[j] = prev + 1
                    ans = max(ans, dp[j])
                else:
                    dp[j] = 0
                prev = temp
        return ans
