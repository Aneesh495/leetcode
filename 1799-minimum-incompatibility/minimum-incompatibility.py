from collections import Counter
from itertools import combinations
from functools import lru_cache
class Solution:
    def minimumIncompatibility(self, nums, k):
        if max(Counter(nums).values())>k: return -1
        n=len(nums); size=n//k; groups=[[] for _ in nums]
        for ids in combinations(range(n),size):
            vals=[nums[i] for i in ids]
            if len(set(vals))<size: continue
            mask=sum(1<<i for i in ids); cost=max(vals)-min(vals)
            for i in ids: groups[i].append((mask,cost))
        full=(1<<n)-1
        @lru_cache(None)
        def dfs(mask):
            if mask==full: return 0
            bit=(~mask&full)&-(~mask&full); i=bit.bit_length()-1
            return min((cost+dfs(mask|g) for g,cost in groups[i] if not (g&mask)),default=float("inf"))
        ans=dfs(0)
        return ans if ans<float("inf") else -1