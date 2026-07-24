class Solution:
    def minRotations(self, n: int, s: str) -> int:
        digits = list(map(int, s))
        last = digits[-1]

        def distance(a, b):
            delta = abs(a - b)
            return min(delta, 10 - delta)

        previous = 0
        baseline = 0
        best_delta = 0
        for current in digits:
            original = distance(previous, current)
            baseline += original
            # Reversing a suffix preserves all its internal distances.
            best_delta = min(best_delta, distance(previous, last) - original)
            previous = current
        return baseline + best_delta