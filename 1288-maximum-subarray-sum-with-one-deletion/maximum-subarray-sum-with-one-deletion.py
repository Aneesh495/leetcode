from typing import List

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        no_del = arr[0]
        one_del = float("-inf")
        ans = arr[0]

        for i in range(1, len(arr)):
            one_del = max(one_del + arr[i], no_del)
            no_del = max(no_del + arr[i], arr[i])
            ans = max(ans, no_del, one_del)

        return ans
