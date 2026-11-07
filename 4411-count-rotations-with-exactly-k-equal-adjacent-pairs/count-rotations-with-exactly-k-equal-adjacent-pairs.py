class Solution:
    def countRotations(self, s: str, k: int) -> int:
        circular_equal = sum(s[i] == s[i - 1] for i in range(len(s)))
        # Rotation at i removes exactly one edge from the circular arrangement.
        return sum(circular_equal - (s[i] == s[i - 1]) == k for i in range(len(s)))