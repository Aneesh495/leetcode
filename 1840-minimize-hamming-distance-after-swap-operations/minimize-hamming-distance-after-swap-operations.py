from collections import Counter, defaultdict
class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps):
        p=list(range(len(source))); size=[1]*len(p)
        def find(x):
            while p[x]!=x: p[x]=p[p[x]]; x=p[x]
            return x
        for a,b in allowedSwaps:
            a=find(a); b=find(b)
            if a!=b:
                if size[a]<size[b]: a,b=b,a
                p[b]=a; size[a]+=size[b]
        groups=defaultdict(Counter)
        for i,x in enumerate(source): groups[find(i)][x]+=1
        ans=0
        for i,x in enumerate(target):
            c=groups[find(i)]
            if c[x]: c[x]-=1
            else: ans+=1
        return ans