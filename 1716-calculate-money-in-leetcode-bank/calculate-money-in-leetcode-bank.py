class Solution:
    def totalMoney(self, n):
        w,r=divmod(n,7)
        return 28*w+7*w*(w-1)//2+r*(w+1)+r*(r-1)//2