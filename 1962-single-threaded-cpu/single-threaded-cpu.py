import heapq
from typing import List

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ordered_tasks = sorted(
            (enqueue_time, processing_time, index)
            for index, (enqueue_time, processing_time) in enumerate(tasks)
            )
        available = []
        current_time = 0
        next_task = 0
        order = []
        task_count = len(ordered_tasks)
        while next_task < task_count or available:
            while (
                next_task < task_count
                and ordered_tasks[next_task][0] <= current_time
            ):
                _, processing_time, original_index = ordered_tasks[next_task]
                heapq.heappush(available, (processing_time, original_index))
                next_task += 1
            if not available:
                current_time = ordered_tasks[next_task][0]
                continue
            processing_time, original_index = heapq.heappop(available)
            order.append(original_index)
            current_time += processing_time
        return order