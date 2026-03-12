
from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Pair each project as (required_capital, profit) then sort by required capital ascending
        projects = sorted(zip(capital, profits))
        
        # Max heap of available profits
        # Python heapq is a min heap so push negative profits to simulate a max heap
        max_heap: List[int] = []
        
        i = 0  # pointer over projects sorted by capital
        n = len(projects)
        
        # Perform at most k selections
        for _ in range(k):
            # Add all projects whose required capital is <= current capital w
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1
            
            # If no available project can be started break early
            if not max_heap:
                break
            
            # Take the most profitable available project and add its profit to capital
            w += -heapq.heappop(max_heap)
        
        return w
