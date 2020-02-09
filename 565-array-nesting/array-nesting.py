
from typing import List

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            if nums[i] != -1:
                cnt = 0
                j = i
                while nums[j] != -1:
                    nxt = nums[j]
                    nums[j] = -1
                    cnt += 1
                    j = nxt
                res = max(res, cnt)
        return res
