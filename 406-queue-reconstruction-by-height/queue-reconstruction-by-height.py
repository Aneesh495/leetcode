
from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Sort by height descending so taller people get placed first
        # For equal height sort by k ascending so smaller k inserts first
        people.sort(key=lambda x: (-x[0], x[1]))
        
        queue: List[List[int]] = []
        # Insert each person at index k
        # Since taller or equal height already placed
        # Inserting at k ensures exactly k taller or equal are in front
        for h, k in people:
            queue.insert(k, [h, k])
        return queue
