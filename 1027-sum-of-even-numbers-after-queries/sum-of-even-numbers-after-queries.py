
from typing import List

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # Compute the initial sum of even numbers
        even_sum = sum(x for x in nums if x % 2 == 0)
        ans: List[int] = []

        for val, idx in queries:
            # If current value at idx is even remove it from the running sum
            if nums[idx] % 2 == 0:
                even_sum -= nums[idx]

            # Apply the query update
            nums[idx] += val

            # If new value at idx is even add it to the running sum
            if nums[idx] % 2 == 0:
                even_sum += nums[idx]

            # Record the sum of even values after this query
            ans.append(even_sum)

        return ans
