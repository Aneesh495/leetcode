class Solution:
    def distanceLimitedPathsExist(self, n, edgeList, queries):
        parent=list(range(n)); size=[1]*n
        def find(x):
            while x!=parent[x]:
                parent[x]=parent[parent[x]]; x=parent[x]
            return x
        edgeList.sort(key=lambda e:e[2]); ans=[False]*len(queries); j=0
        for i,(u,v,limit) in sorted(enumerate(queries),key=lambda x:x[1][2]):
            while j<len(edgeList) and edgeList[j][2]<limit:
                a,b,_=edgeList[j]; a=find(a); b=find(b)
                if a!=b:
                    if size[a]<size[b]: a,b=b,a
                    parent[b]=a; size[a]+=size[b]
                j+=1
            ans[i]=find(u)==find(v)
        return ans