class Solution:
    def maximizeXor(self, nums, queries):
        nums.sort(); root={}; j=0; ans=[-1]*len(queries)
        for i,(x,limit) in sorted(enumerate(queries),key=lambda t:t[1][1]):
            while j<len(nums) and nums[j]<=limit:
                node=root; value=nums[j]
                for b in range(30,-1,-1): node=node.setdefault((value>>b)&1,{})
                j+=1
            if j:
                node=root; score=0
                for b in range(30,-1,-1):
                    bit=(x>>b)&1
                    if 1-bit in node: score|=1<<b; node=node[1-bit]
                    else: node=node[bit]
                ans[i]=score
        return ans