class Solution:
    def minimumTimeRequired(self, jobs, k):
        jobs.sort(reverse=True)
        lo=max(jobs[0],(sum(jobs)+k-1)//k); hi=sum(jobs)
        def feasible(cap):
            loads=[0]*k
            def dfs(i):
                if i==len(jobs): return True
                seen=set()
                for j in range(k):
                    if loads[j] in seen or loads[j]+jobs[i]>cap: continue
                    seen.add(loads[j]); loads[j]+=jobs[i]
                    if dfs(i+1): return True
                    loads[j]-=jobs[i]
                    if loads[j]==0: break
                return False
            return dfs(0)
        while lo<hi:
            mid=(lo+hi)//2
            if feasible(mid): hi=mid
            else: lo=mid+1
        return lo