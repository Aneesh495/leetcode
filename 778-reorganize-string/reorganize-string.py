import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        Reorganize the string so that no two adjacent characters are the same.
        Return an empty string if it is not possible.
        Time O(n log k) where n is len(s) and k is the alphabet size
        Space O(k)
        """

        n = len(s)
        freq = Counter(s)

        # Quick impossibility check
        # If the most frequent char count is greater than ceil(n/2) then impossible
        if max(freq.values()) > (n + 1) // 2:
            return ""

        # Max heap using negative counts since Python has a min heap
        heap = [(-cnt, ch) for ch, cnt in freq.items()]
        heapq.heapify(heap)

        res = []

        # Always take the two most frequent different chars
        # This guarantees no adjacent duplicates and greedily balances counts
        while len(heap) >= 2:
            cnt1, ch1 = heapq.heappop(heap)  # most frequent
            cnt2, ch2 = heapq.heappop(heap)  # second most frequent

            res.append(ch1)
            res.append(ch2)

            # Decrease counts and push back if any remain
            if cnt1 + 1 < 0:
                heapq.heappush(heap, (cnt1 + 1, ch1))
            if cnt2 + 1 < 0:
                heapq.heappush(heap, (cnt2 + 1, ch2))

        # If one char remains it can be placed only if it does not duplicate the last char
        if heap:
            cnt, ch = heapq.heappop(heap)
            # Since we passed the impossibility check this leftover count must be 1
            # Place it at the end if it does not equal the last char
            if not res or res[-1] != ch:
                res.append(ch)
            else:
                return ""

        return "".join(res)