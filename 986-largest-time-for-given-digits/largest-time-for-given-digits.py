
from typing import List
from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        # Try all 4! permutations as HH:MM
        best_total = -1  # track best time in minutes since 00:00
        for h1, h2, m1, m2 in permutations(arr, 4):
            hour = h1 * 10 + h2
            minute = m1 * 10 + m2
            # Validate 24 hour time
            if 0 <= hour < 24 and 0 <= minute < 60:
                total = hour * 60 + minute
                if total > best_total:
                    best_total = total
        # Build formatted result or empty if none valid
        return "" if best_total < 0 else f"{best_total // 60:02d}:{best_total % 60:02d}"
