from bisect import bisect_left
class Solution:
    def minOperations(self, target, arr):
        idx={x:i for i,x in enumerate(target)}; seq=[]
        for x in arr:
            if x in idx:
                v=idx[x]; i=bisect_left(seq,v)
                if i==len(seq): seq.append(v)
                else: seq[i]=v
        return len(target)-len(seq)