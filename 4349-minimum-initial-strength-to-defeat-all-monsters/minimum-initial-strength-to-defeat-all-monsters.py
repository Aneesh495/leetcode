from itertools import accumulate

class Solution:
    def minInitialStrength(self, monsters: list[int], boosts: list[list[int]]) -> int:
        changes = [0] * (len(monsters) + 1)
        for start, end, extra in boosts:
            changes[start] += extra
            changes[end + 1] -= extra
        bonuses = list(accumulate(changes))
        required = 0
        for i in range(len(monsters) - 1, -1, -1):
            # A positive future requirement must remain after the monster's full cost.
            if required > 0:
                required += monsters[i]
            else:
                required = max(0, monsters[i] - bonuses[i])
        return required