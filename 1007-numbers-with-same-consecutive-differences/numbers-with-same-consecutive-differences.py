
from typing import List
from collections import deque

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        """
        Build all length-n integers where the absolute difference between every
        pair of adjacent digits equals k. No leading zeros allowed for n > 1.
        BFS grows numbers digit by digit.
        """
        # Base seeds
        if n == 1:
            # Single-digit numbers are all valid
            return [i for i in range(10)]

        # Start from digits 1..9 to avoid leading zero
        q = deque(range(1, 10))
        length = 1

        while length < n:
            for _ in range(len(q)):
                num = q.popleft()
                last = num % 10

                # Next possible digits that keep |diff| == k
                cand1 = last + k
                cand2 = last - k

                # Add cand1 if within 0..9
                if 0 <= cand1 <= 9:
                    q.append(num * 10 + cand1)

                # Add cand2 if within 0..9 and different from cand1
                if k != 0 and 0 <= cand2 <= 9:
                    q.append(num * 10 + cand2)

            length += 1

        return list(q)
