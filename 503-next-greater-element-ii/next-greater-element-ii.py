
from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        Monotonic decreasing stack over indices
        Traverse the circular array twice using modulo
        Time O(n) Space O(n)
        """
        n = len(nums)
        ans = [-1] * n                   # default when no greater element exists
        st = []                          # stack holds indices whose NGE not found yet

        # iterate 0 to 2n - 1 to simulate circularity
        for i in range(2 * n):
            j = i % n                    # real index in nums
            # while current value beats stack top assign it as the next greater
            while st and nums[j] > nums[st[-1]]:
                ans[st.pop()] = nums[j]
            # push only during the first pass
            if i < n:
                st.append(j)

        return ans
