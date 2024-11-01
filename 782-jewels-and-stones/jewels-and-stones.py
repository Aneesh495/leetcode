
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jset = set(jewels)
        return sum(c in jset for c in stones)
