
from typing import List

class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return n

        # next_higher[i] = next index j to jump to on an odd jump from i
        # It must be the smallest index j with arr[j] >= arr[i] and minimal arr[j]
        # next_lower[i] = next index j to jump to on an even jump from i
        # It must be the smallest index j with arr[j] <= arr[i] and maximal arr[j]
        next_higher = [-1] * n
        next_lower = [-1] * n

        # Helper to compute next indices using a monotonic stack over a specific ordering
        def build_next(order: List[int]) -> List[int]:
            res = [-1] * n
            stack = []
            for i in order:
                # Maintain increasing indices in stack; when we find a greater index i
                # we assign i as the "next" for the top since order guarantees the value rule
                while stack and i > stack[-1]:
                    res[stack.pop()] = i
                stack.append(i)
            return res

        # Order for odd jumps: sort by value asc then index asc
        order_odd = sorted(range(n), key=lambda i: (arr[i], i))
        next_higher = build_next(order_odd)

        # Order for even jumps: sort by value desc then index asc
        order_even = sorted(range(n), key=lambda i: (-arr[i], i))
        next_lower = build_next(order_even)

        # DP: odd[i] true if starting at i with an odd jump can reach end
        #      even[i] true if starting at i with an even jump can reach end
        odd = [False] * n
        even = [False] * n
        odd[-1] = True
        even[-1] = True

        for i in range(n - 2, -1, -1):
            j = next_higher[i]
            if j != -1:
                odd[i] = even[j]
            j = next_lower[i]
            if j != -1:
                even[i] = odd[j]

        return sum(odd)
