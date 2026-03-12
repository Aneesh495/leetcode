
from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # Iterative DFS over the implicit 10-ary tree of prefixes
        # Time O(n) Space O(1) excluding output
        res: List[int] = []
        curr = 1
        for _ in range(n):
            res.append(curr)
            # Dive to smallest lexicographic child if possible
            if curr * 10 <= n:
                curr *= 10
            else:
                # Otherwise climb up until we can move to the next sibling
                while curr % 10 == 9 or curr + 1 > n:
                    curr //= 10
                curr += 1
        return res
