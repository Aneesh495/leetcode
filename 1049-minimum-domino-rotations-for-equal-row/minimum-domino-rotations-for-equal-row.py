
from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        """
        Goal
        Make all values in either the top row or the bottom row equal using the fewest rotations
        A rotation swaps the two values within the same domino

        Key fact
        If a solution exists then every domino must contain the target value
        Therefore the only possible targets are tops[0] or bottoms[0]
        Check both targets and take the minimum valid rotation count
        """

        def rotations_to_make(target: int) -> int:
            """
            Try to make all tops equal to target or all bottoms equal to target
            Count how many rotations are needed for each case
            If any domino lacks target on both halves then it is impossible
            """
            rotate_top = 0   # rotations to make all of tops == target
            rotate_bot = 0   # rotations to make all of bottoms == target

            for t, b in zip(tops, bottoms):
                if t != target and b != target:
                    return float("inf")  # impossible for this target
                if t != target:
                    # put target on top by rotating this domino
                    rotate_top += 1
                if b != target:
                    # put target on bottom by rotating this domino
                    rotate_bot += 1

            # You can make either the top row or the bottom row uniform
            return min(rotate_top, rotate_bot)

        cand1 = rotations_to_make(tops[0])
        cand2 = rotations_to_make(bottoms[0])
        ans = min(cand1, cand2)
        return -1 if ans == float("inf") else ans
