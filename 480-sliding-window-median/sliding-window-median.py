
from typing import List
import heapq
from collections import defaultdict

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # Two heaps with lazy deletion
        # lo stores the smaller half as a max heap using negative values
        # hi stores the larger half as a min heap
        lo, hi = [], []
        delayed = defaultdict(int)  # value -> pending deletions count
        lo_size = 0  # number of valid elements in lo
        hi_size = 0  # number of valid elements in hi

        def prune(heap):
            # Remove invalid elements from the top of the given heap
            while heap:
                x = heap[0]
                val = -x if heap is lo else x
                if delayed[val]:
                    heapq.heappop(heap)
                    delayed[val] -= 1
                    if delayed[val] == 0:
                        del delayed[val]
                else:
                    break

        def rebalance():
            # Keep sizes within one of each other and ensure lo has the extra when k is odd
            nonlocal lo_size, hi_size
            if lo_size > hi_size + 1:
                # move top from lo to hi
                val = -heapq.heappop(lo)
                heapq.heappush(hi, val)
                lo_size -= 1
                hi_size += 1
                prune(lo)
            elif lo_size < hi_size:
                # move top from hi to lo
                val = heapq.heappop(hi)
                heapq.heappush(lo, -val)
                hi_size -= 1
                lo_size += 1
                prune(hi)

        def add_num(x):
            nonlocal lo_size, hi_size
            if not lo or x <= -lo[0]:
                heapq.heappush(lo, -x)
                lo_size += 1
            else:
                heapq.heappush(hi, x)
                hi_size += 1
            rebalance()

        def remove_num(x):
            nonlocal lo_size, hi_size
            delayed[x] += 1
            if x <= -lo[0]:
                lo_size -= 1
                if x == -lo[0]:
                    prune(lo)
            else:
                hi_size -= 1
                if hi and x == hi[0]:
                    prune(hi)
            rebalance()

        def get_median():
            if k % 2 == 1:
                return float(-lo[0])
            else:
                return (-lo[0] + hi[0]) / 2.0

        # Initialize the first window
        for i in range(k):
            add_num(nums[i])

        ans = [get_median()]

        # Slide the window
        for i in range(k, len(nums)):
            add_num(nums[i])
            remove_num(nums[i - k])
            ans.append(get_median())

        return ans
