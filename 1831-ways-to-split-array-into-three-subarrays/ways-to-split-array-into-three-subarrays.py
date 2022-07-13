from itertools import accumulate
from bisect import bisect_left, bisect_right
class Solution:
    def waysToSplit(self, nums):
        p=list(accumulate(nums)); n=len(nums); ans=0
        for i in range(n-2):
            lo=bisect_left(p,2*p[i],i+1,n-1)
            hi=bisect_right(p,(p[-1]+p[i])//2,i+1,n-1)
            ans+=max(0,hi-lo)
        return ans%1000000007