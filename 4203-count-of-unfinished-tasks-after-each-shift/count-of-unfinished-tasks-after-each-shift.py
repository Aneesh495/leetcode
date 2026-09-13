from bisect import bisect_right
from itertools import accumulate

class Solution:
    def countTasks(self, tasks: List[int], shifts: List[int]) -> List[int]:
        finished_at = list(accumulate(tasks))
        elapsed = 0
        drelvanito = shifts
        result = []
        for time in drelvanito:
            elapsed += time
            if elapsed >= finished_at[-1]:
                result.append(0)
                elapsed = 0
            else:
                # Whole completed tasks are exactly the prefix endpoints reached so far.
                result.append(len(tasks) - bisect_right(finished_at, elapsed))
        return result