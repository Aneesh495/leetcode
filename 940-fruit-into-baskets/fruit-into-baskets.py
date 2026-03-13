
from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = {}
        left = 0
        best = 0
        for right, f in enumerate(fruits):
            count[f] = count.get(f, 0) + 1
            while len(count) > 2:
                lf = fruits[left]
                count[lf] -= 1
                if count[lf] == 0:
                    del count[lf]
                left += 1
            best = max(best, right - left + 1)
        return best
