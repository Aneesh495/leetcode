
from collections import Counter
from typing import List

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        """
        Greedy pairing using counts.
        Key idea:
          - Pair each x with 2*x
          - Process numbers in increasing order of absolute value
            so smaller magnitudes claim their doubles first
          - Handle zeros by requiring an even count
        Time: O(n log n) due to sorting unique values
        Space: O(n) for counts
        """
        cnt = Counter(arr)

        # Zeros must come in pairs
        if cnt[0] % 2:
            return False

        # Process by absolute value so negatives work correctly
        for x in sorted(cnt.keys(), key=abs):
            if cnt[x] == 0:
                continue
            need = cnt[x]
            # If not enough doubles remain then impossible
            if cnt[2 * x] < need:
                return False
            cnt[2 * x] -= need  # Commit the pairing

        return True
