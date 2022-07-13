from collections import defaultdict
class Solution:
    def countPairs(self, deliciousness):
        seen=defaultdict(int); ans=0
        for x in deliciousness:
            for i in range(22): ans+=seen[(1<<i)-x]
            seen[x]+=1
        return ans%1000000007