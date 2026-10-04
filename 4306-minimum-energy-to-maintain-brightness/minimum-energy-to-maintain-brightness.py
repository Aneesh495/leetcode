class Solution:
    def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:
        # One bulb covers at most three positions. Consecutive blocks attain that bound.
        bulbs = (brightness + 2) // 3

        # Count each covered time unit once by merging overlapping intervals.
        ordered = sorted(intervals)
        left, right = ordered[0]
        active = 0
        for start, end in ordered[1:]:
            if start > right:
                active += right - left + 1
                left, right = start, end
            else:
                right = max(right, end)
        return bulbs * (active + right - left + 1)