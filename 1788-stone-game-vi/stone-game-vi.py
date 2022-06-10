class Solution:
    def stoneGameVI(self, aliceValues, bobValues):
        pairs=sorted(zip(aliceValues,bobValues),key=lambda p:sum(p),reverse=True)
        diff=sum(a if i%2==0 else -b for i,(a,b) in enumerate(pairs))
        return (diff>0)-(diff<0)