class Solution:
    def getSumAbsoluteDifferences(self, nums):
        total=sum(nums); pre=0; ans=[]; n=len(nums)
        for i,x in enumerate(nums):
            ans.append(x*i-pre + total-pre-x-x*(n-i-1))
            pre+=x
        return ans