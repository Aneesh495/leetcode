
from typing import List
from collections import Counter, defaultdict

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        need = defaultdict(int)
        for x in nums:
            if freq[x] == 0:
                continue
            if need[x] > 0:
                need[x] -= 1
                need[x + 1] += 1
                freq[x] -= 1
            elif freq[x + 1] > 0 and freq[x + 2] > 0:
                freq[x] -= 1
                freq[x + 1] -= 1
                freq[x + 2] -= 1
                need[x + 3] += 1
            else:
                return False
        return True
