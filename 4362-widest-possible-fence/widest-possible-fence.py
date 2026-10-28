from collections import Counter

class Solution:
    def maximumWidth(self, planks: list[int]) -> int:
        frequency = Counter(planks)
        choices = list(frequency.items())
        width = dict(frequency)
        for i, (height, count) in enumerate(choices):
            if count >= 2:
                doubled = 2 * height
                width[doubled] = width.get(doubled, 0) + count // 2
            for j in range(i):
                other, available = choices[j]
                combined = height + other
                # At a fixed height, an original height has only one possible complement.
                width[combined] = width.get(combined, 0) + min(count, available)
        return max(width.values())