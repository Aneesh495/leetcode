
from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Both arrays are sorted nondecreasing
        # Use a min heap of tuples (sum, i, j) where i indexes nums1 and j indexes nums2
        res = []
        if not nums1 or not nums2 or k <= 0:
            return res

        n1 = len(nums1)
        n2 = len(nums2)

        # Seed heap with pairs (i, 0) for first min(k, n1) elements from nums1
        heap = []
        limit = min(k, n1)
        for i in range(limit):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        # Extract k pairs with smallest sums
        while heap and len(res) < k:
            s, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])

            # Next pair with same i is (i, j+1)
            if j + 1 < n2:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return res
