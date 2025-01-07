
from collections import defaultdict, deque
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        stop_to_routes = defaultdict(list)
        for i, r in enumerate(routes):
            for stop in r:
                stop_to_routes[stop].append(i)

        q = deque([source])
        visited_routes = set()
        visited_stops = {source}
        buses = 0

        while q:
            buses += 1
            for _ in range(len(q)):
                s = q.popleft()
                for ri in stop_to_routes.get(s, []):
                    if ri in visited_routes:
                        continue
                    visited_routes.add(ri)
                    for nxt in routes[ri]:
                        if nxt == target:
                            return buses
                        if nxt not in visited_stops:
                            visited_stops.add(nxt)
                            q.append(nxt)
        return -1
