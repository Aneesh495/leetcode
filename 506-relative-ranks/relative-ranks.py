
from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        res = [""] * n
        order = sorted(range(n), key=lambda i: score[i], reverse=True)
        for rank, idx in enumerate(order, start=1):
            if rank == 1:
                res[idx] = "Gold Medal"
            elif rank == 2:
                res[idx] = "Silver Medal"
            elif rank == 3:
                res[idx] = "Bronze Medal"
            else:
                res[idx] = str(rank)
        return res
