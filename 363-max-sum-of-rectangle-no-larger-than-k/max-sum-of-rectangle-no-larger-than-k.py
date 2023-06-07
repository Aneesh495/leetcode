
from typing import List
from bisect import bisect_left, insort

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        # Choose the smaller dimension for the outer loops to reduce time
        rows, cols = len(matrix), len(matrix[0])
        if rows > cols:
            # Transpose to make rows the smaller side
            matrix = [list(r) for r in zip(*matrix)]
            rows, cols = cols, rows

        ans = float("-inf")

        # Prefix sums over columns for each fixed pair of top and bottom rows
        for top in range(rows):
            col_sums = [0] * cols
            for bottom in range(top, rows):
                # Accumulate row values into column sums
                for c in range(cols):
                    col_sums[c] += matrix[bottom][c]

                # Find the best subarray sum no larger than k in col_sums
                # Use prefix sums and a sorted list with binary search
                prefix = 0
                prefixes = [0]
                best = float("-inf")
                for val in col_sums:
                    prefix += val
                    # We want smallest prefix >= prefix - k
                    target = prefix - k
                    i = bisect_left(prefixes, target)
                    if i < len(prefixes):
                        best = max(best, prefix - prefixes[i])
                        if best == k:
                            return k
                    insort(prefixes, prefix)

                ans = max(ans, best)
                if ans == k:
                    return k

        return ans
