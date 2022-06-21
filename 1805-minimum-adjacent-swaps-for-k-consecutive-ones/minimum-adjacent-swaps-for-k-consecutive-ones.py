from itertools import accumulate
class Solution:
    def minMoves(self, nums, k):
        positions=[i for i,x in enumerate(nums) if x]
        a=[p-i for i,p in enumerate(positions)]
        pref=[0]+list(accumulate(a)); ans=float("inf")
        for l in range(len(a)-k+1):
            r=l+k; m=l+k//2; v=a[m]
            cost=v*(m-l)-(pref[m]-pref[l])+(pref[r]-pref[m+1])-v*(r-m-1)
            ans=min(ans,cost)
        return ans