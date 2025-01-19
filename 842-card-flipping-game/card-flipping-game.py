
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        bad = {x for x, y in zip(fronts, backs) if x == y}
        ans = float('inf')
        for x in fronts + backs:
            if x not in bad:
                ans = min(ans, x)
        return 0 if ans == float('inf') else ans
