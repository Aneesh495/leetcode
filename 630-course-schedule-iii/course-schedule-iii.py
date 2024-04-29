
import heapq
from typing import List

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        max_heap = []
        time = 0
        for d, end in courses:
            time += d
            heapq.heappush(max_heap, -d)
            if time > end:
                time += heapq.heappop(max_heap)
        return len(max_heap)
