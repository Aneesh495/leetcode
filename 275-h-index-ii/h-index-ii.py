
# LeetCode 275 H-Index II
# Binary search on sorted citations
# Find smallest index i with citations[i] >= n - i
# Answer is n - i. If none found the answer is 0

from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left = 0
        right = n - 1
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            h = n - mid
            if citations[mid] >= h:
                ans = h            # valid h found. try to increase by moving left
                right = mid - 1
            else:
                left = mid + 1     # need larger citations. move right
        return ans
