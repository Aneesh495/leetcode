
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Boyer Moore majority vote generalized for elements appearing more than n//3
        # There can be at most two such elements
        cand1 = None
        cand2 = None
        cnt1 = 0
        cnt2 = 0

        # First pass selects up to two candidates
        for x in nums:
            if cand1 == x:
                cnt1 += 1
            elif cand2 == x:
                cnt2 += 1
            elif cnt1 == 0:
                cand1 = x
                cnt1 = 1
            elif cnt2 == 0:
                cand2 = x
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        # Second pass verifies the actual counts
        res = []
        n = len(nums)
        c1 = sum(1 for v in nums if v == cand1)
        c2 = sum(1 for v in nums if v == cand2) if cand2 is not None else 0
        if cand1 is not None and c1 > n // 3:
            res.append(cand1)
        if cand2 is not None and cand2 != cand1 and c2 > n // 3:
            res.append(cand2)
        return res
