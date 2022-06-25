from itertools import accumulate
class Solution:
    def stoneGameVII(self, stones):
        n=len(stones); pref=[0]+list(accumulate(stones)); dp=[0]*n
        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                dp[j]=max(pref[j+1]-pref[i+1]-dp[j], pref[j]-pref[i]-dp[j-1])
        return dp[-1]