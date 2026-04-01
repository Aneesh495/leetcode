
from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Maintain a max heap of size k using negative distances
        # Each entry is (-squared_distance, x, y)
        heap: List[tuple[int, int, int]] = []
        for x, y in points:
            d = x * x + y * y  # squared distance to avoid sqrt
            if len(heap) < k:
                heapq.heappush(heap, (-d, x, y))
            else:
                # If this point is closer than the farthest in heap replace it
                if d < -heap[0][0]:
                    heapq.heapreplace(heap, (-d, x, y))
        # Extract k points from heap
        return [[x, y] for _, x, y in heap]
