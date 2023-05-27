
from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count each value
        freq = Counter(nums)

        # Bucket by frequency. Index i stores all numbers that appear i times
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            buckets[count].append(num)

        # Collect from highest frequency down until k elements are gathered
        res: List[int] = []
        for count in range(len(nums), 0, -1):
            for num in buckets[count]:
                res.append(num)
                if len(res) == k:
                    return res

        return res
