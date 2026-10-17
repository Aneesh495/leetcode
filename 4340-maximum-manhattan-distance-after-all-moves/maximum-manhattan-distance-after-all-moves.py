class Solution:
    def maxDistance(self, moves: str) -> int:
        horizontal = moves.count('R') - moves.count('L')
        vertical = moves.count('U') - moves.count('D')
        # Every wildcard can extend the final displacement by one unit.
        return abs(horizontal) + abs(vertical) + moves.count('_')