
from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # tails[i] holds the minimum possible tail value of an increasing subsequence of length i+1
        tails = []
        for x in nums:
            # find the first index in tails where tails[idx] >= x
            idx = bisect.bisect_left(tails, x)
            if idx == len(tails):
                # x extends the longest subsequence found so far
                tails.append(x)
            else:
                # x improves the tail of a subsequence of length idx+1
                tails[idx] = x
        # the size of tails equals the LIS length
        return len(tails)
