class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        from math import gcd
        return [f"{a}/{b}" for b in range(2,n+1) for a in range(1,b) if gcd(a,b)==1]