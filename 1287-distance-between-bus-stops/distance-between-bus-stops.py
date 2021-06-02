from typing import List

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        
        clockwise = sum(distance[start:destination])
        total = sum(distance)
        
        return min(clockwise, total - clockwise)
