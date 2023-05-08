
from typing import List
from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        LeetCode 332 Reconstruct Itinerary
        Requirements
          • Use all tickets exactly once
          • Start at "JFK"
          • If multiple valid itineraries exist return the one with smallest lexical order
        Approach
          • Build a directed multigraph where edges are tickets
          • For each origin keep a min heap of destinations so we always take the smallest next airport
          • Run Hierholzer’s algorithm to get an Eulerian path then reverse the result
        """

        # Build adjacency with min heaps for lexical order
        graph = defaultdict(list)              # origin -> min heap of destinations
        for a, b in tickets:
            heapq.heappush(graph[a], b)

        route = []                              # will collect airports in reverse postorder
        stack = ["JFK"]                         # iterative DFS to avoid recursion depth issues

        while stack:
            cur = stack[-1]
            # While there are unused outgoing tickets pick the lexicographically smallest destination
            if graph[cur]:
                nxt = heapq.heappop(graph[cur])
                stack.append(nxt)
            else:
                # No more outgoing edges from cur
                # Add to route and backtrack
                route.append(stack.pop())

        # route is built in reverse
        return route[::-1]
