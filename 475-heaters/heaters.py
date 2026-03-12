
from bisect import bisect_left
from typing import List

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # Sort both arrays so positions are ordered
        houses.sort()
        heaters.sort()

        # For binary search convenience add sentinels at extremes
        # Use very negative and very positive sentinels so every house has two neighbors
        INF = 10**18
        heaters = [-INF] + heaters + [INF]

        ans = 0
        for x in houses:
            # idx is the first heater whose position is not less than x
            idx = bisect_left(heaters, x)
            # Two nearest heaters are heaters[idx - 1] and heaters[idx]
            left_dist = x - heaters[idx - 1]
            right_dist = heaters[idx] - x
            # Minimum distance to a heater for this house
            need = min(left_dist, right_dist)
            # Required radius is the maximum over all houses
            if need > ans:
                ans = need

        return ans
