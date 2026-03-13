
from collections import Counter
from math import ceil
from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        total = 0
        for x, c in count.items():
            group = x + 1
            groups_needed = (c + group - 1) // group
            total += groups_needed * group
        return total
