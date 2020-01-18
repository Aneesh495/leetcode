
from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > 1440:
            return 0
        minutes = []
        for t in timePoints:
            h = int(t[:2])
            m = int(t[3:])
            minutes.append(h * 60 + m)
        minutes.sort()
        ans = 1440
        for i in range(1, len(minutes)):
            ans = min(ans, minutes[i] - minutes[i - 1])
        ans = min(ans, 1440 - (minutes[-1] - minutes[0]))
        return ans
