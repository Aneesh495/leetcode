class Solution:
    def maximumUniqueSubarray(self, nums):
        seen=set(); left=total=ans=0
        for x in nums:
            while x in seen:
                y=nums[left]; left+=1; seen.remove(y); total-=y
            seen.add(x); total+=x; ans=max(ans,total)
        return ans