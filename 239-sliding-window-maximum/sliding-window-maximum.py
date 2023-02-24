
from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Deque will store indices of elements
        # It will be kept in decreasing order of values nums[idx]
        dq = deque()
        res: List[int] = []

        for i, x in enumerate(nums):
            # 1) Remove indices that are out of the current window [i - k + 1, i]
            while dq and dq[0] <= i - k:
                dq.popleft()

            # 2) Maintain decreasing order. Remove smaller values from the back
            while dq and nums[dq[-1]] <= x:
                dq.pop()

            # 3) Add current index
            dq.append(i)

            # 4) Record the max for windows that have reached size k
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res
