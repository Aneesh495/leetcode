
from typing import List

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        MAX_AGE = 120
        cnt = [0] * (MAX_AGE + 1)
        for a in ages:
            cnt[a] += 1

        prefix = [0] * (MAX_AGE + 1)
        for i in range(1, MAX_AGE + 1):
            prefix[i] = prefix[i - 1] + cnt[i]

        res = 0
        for a in range(15, MAX_AGE + 1):
            if cnt[a] == 0:
                continue
            low = a // 2 + 8  # first b such that b > 0.5*a + 7
            high = a
            if low > high:
                continue
            total_in_range = prefix[high] - prefix[low - 1]
            res += cnt[a] * (total_in_range - 1)  # exclude self
        return res
