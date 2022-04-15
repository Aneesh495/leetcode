class Solution:
    def constructDistancedSequence(self, n):
        a=[0]*(2*n-1)
        def dfs(i,used):
            while i<len(a) and a[i]: i+=1
            if i==len(a): return True
            for x in range(n,0,-1):
                if used>>x&1: continue
                j=i+x if x>1 else i
                if j>=len(a) or a[j]: continue
                a[i]=a[j]=x
                if dfs(i+1,used|1<<x): return True
                a[i]=a[j]=0
            return False
        dfs(0,0)
        return a