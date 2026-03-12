
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        Binary search on value space
        Count how many elements are less than or equal to mid in O(n)
        Matrix rows and columns are sorted in nondecreasing order
        """

        n = len(matrix)
        low = matrix[0][0]               # smallest value in matrix
        high = matrix[-1][-1]            # largest value in matrix

        def count_le(x: int) -> int:
            """
            Return how many elements in matrix are less than or equal to x
            Walk from top right to bottom left counting elements per row
            """
            cnt = 0
            r = 0
            c = n - 1
            while r < n and c >= 0:
                if matrix[r][c] <= x:
                    # all numbers in this column to the left are <= x for this row
                    cnt += c + 1
                    r += 1
                else:
                    c -= 1
            return cnt

        # standard lower bound search for the smallest value with count >= k
        while low < high:
            mid = (low + high) // 2
            if count_le(mid) >= k:
                high = mid
            else:
                low = mid + 1

        return low
