
from typing import List
import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        heap = []
        cur_max = float('-inf')
        for i, arr in enumerate(nums):
            v = arr[0]
            heap.append((v, i, 0))
            if v > cur_max:
                cur_max = v
        heapq.heapify(heap)

        best_l, best_r = heap[0][0], cur_max

        while True:
            v, r, c = heapq.heappop(heap)
            if cur_max - v < best_r - best_l or (cur_max - v == best_r - best_l and v < best_l):
                best_l, best_r = v, cur_max
            if c + 1 == len(nums[r]):
                break
            nv = nums[r][c + 1]
            if nv > cur_max:
                cur_max = nv
            heapq.heappush(heap, (nv, r, c + 1))

        return [best_l, best_r]
