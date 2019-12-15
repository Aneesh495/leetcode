
# LeetCode 495. Teemo Attacking
# Time O(n) where n is len(timeSeries)
# Space O(1)
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        # If there are no attacks then total poisoned time is zero
        if not timeSeries:
            return 0

        total = 0
        # For each attack except the last add the non overlapping contribution
        # The effect from an attack at t lasts until t + duration
        # If the next attack happens before that end only the gap counts
        for i in range(len(timeSeries) - 1):
            gap = timeSeries[i + 1] - timeSeries[i]
            total += min(duration, gap)

        # Add full duration for the last attack
        total += duration
        return total
