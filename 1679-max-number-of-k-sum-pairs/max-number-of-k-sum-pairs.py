from collections import Counter
class Solution:
    def maxOperations(self, nums, k):
        c=Counter(nums); ans=0
        for x in c:
            if x<k-x: ans+=min(c[x],c[k-x])
            elif x==k-x: ans+=c[x]//2
        return ans