from collections import deque
class Solution:
    def boxDelivering(self, boxes, portsCount, maxBoxes, maxWeight):
        n=len(boxes); w=[0]*(n+1); c=[0]*(n+1)
        for i,(p,weight) in enumerate(boxes,1):
            w[i]=w[i-1]+weight
            c[i]=c[i-1]+(i>1 and p!=boxes[i-2][0])
        dp=[0]*(n+1); q=deque([0])
        for i in range(1,n+1):
            while q and (i-q[0]>maxBoxes or w[i]-w[q[0]]>maxWeight): q.popleft()
            j=q[0]; dp[i]=dp[j]+c[i]-c[j+1]+2
            if i<n:
                value=dp[i]-c[i+1]
                while q and dp[q[-1]]-c[q[-1]+1]>=value: q.pop()
                q.append(i)
        return dp[n]