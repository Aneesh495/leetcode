
from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        idx = {s: i for i, s in enumerate(list1)}
        res = []
        best = float('inf')
        for j, s in enumerate(list2):
            if s in idx:
                total = j + idx[s]
                if total < best:
                    best = total
                    res = [s]
                elif total == best:
                    res.append(s)
        return res
