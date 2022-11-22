class Solution:
    def mergeTriplets(self, triplets, target):
        seen=[False]*3
        for t in triplets:
            if all(a<=b for a,b in zip(t,target)):
                for i in range(3): seen[i]|=t[i]==target[i]
        return all(seen)