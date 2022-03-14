from functools import cache
class Solution:
    def minCost(self, n: int, cuts: list[int]) -> int:
        a = [0] + sorted(cuts) + [n]
        @cache
        def dp(i,j):
            if j == i+1: return 0
            return a[j]-a[i] + min(dp(i,k)+dp(k,j) for k in range(i+1,j))
        return dp(0,len(a)-1)