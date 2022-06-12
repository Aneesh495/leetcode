class Solution:
    def minMoves(self, nums, limit):
        d=[0]*(2*limit+3)
        for i in range(len(nums)//2):
            a,b=nums[i],nums[-1-i]
            d[2]+=2
            d[min(a,b)+1]-=1
            d[a+b]-=1
            d[a+b+1]+=1
            d[max(a,b)+limit+1]+=1
        cur=0; best=len(nums)
        for x in d[2:2*limit+1]:
            cur+=x; best=min(best,cur)
        return best