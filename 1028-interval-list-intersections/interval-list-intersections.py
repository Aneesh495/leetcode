
from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
        Two pointer sweep across both sorted interval lists.
        At each step compute overlap start as max of starts and end as min of ends.
        If start <= end then an intersection exists so record it.
        Advance the pointer of the interval that ends first since it cannot intersect anything further.
        Time O(n + m). Space O(1) extra besides output.
        """
        i = j = 0
        res: List[List[int]] = []

        while i < len(firstList) and j < len(secondList):
            a_start, a_end = firstList[i]
            b_start, b_end = secondList[j]

            start = max(a_start, b_start)
            end = min(a_end, b_end)

            if start <= end:
                res.append([start, end])

            if a_end < b_end:
                i += 1
            else:
                j += 1

        return res
