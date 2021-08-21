class Solution:
    def maxHeight(self, cuboids):
        c=sorted(sorted(x) for x in cuboids); dp=[]
        for i,(a,b,h) in enumerate(c):
            dp.append(h+max((dp[j] for j,(x,y,z) in enumerate(c[:i]) if x<=a and y<=b and z<=h),default=0))
        return max(dp)